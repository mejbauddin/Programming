import argparse
import base64
import ipaddress
import secrets
import shutil
import sqlite3
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Optional


APP_DIR = Path(__file__).resolve().parent
DB_PATH = APP_DIR / "wg_manager.db"


def _new_key() -> str:
    return base64.b64encode(secrets.token_bytes(32)).decode("ascii")


def _wg_executable() -> Optional[str]:
    return shutil.which("wg") or shutil.which("wg.exe")


def _generate_wg_keypair() -> tuple[str, str]:
    wg_bin = _wg_executable()
    if not wg_bin:
        # Fallback keeps development flow working, but real deployment should use wg.
        private_key = _new_key()
        public_key = _new_key()
        return private_key, public_key
    private = subprocess.run(
        [wg_bin, "genkey"], capture_output=True, text=True, check=True
    ).stdout.strip()
    public = subprocess.run(
        [wg_bin, "pubkey"],
        input=private + "\n",
        capture_output=True,
        text=True,
        check=True,
    ).stdout.strip()
    return private, public


def _init_db() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS settings (
            key TEXT PRIMARY KEY,
            value TEXT NOT NULL
        )
        """
    )
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS peers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            private_key TEXT NOT NULL,
            public_key TEXT NOT NULL,
            assigned_ip TEXT UNIQUE NOT NULL,
            active INTEGER NOT NULL DEFAULT 1
        )
        """
    )
    conn.commit()
    return conn


def _set_setting(conn: sqlite3.Connection, key: str, value: str) -> None:
    conn.execute(
        "INSERT INTO settings(key, value) VALUES(?, ?) ON CONFLICT(key) DO UPDATE SET value = excluded.value",
        (key, value),
    )
    conn.commit()


def _get_setting(conn: sqlite3.Connection, key: str) -> Optional[str]:
    row = conn.execute("SELECT value FROM settings WHERE key = ?", (key,)).fetchone()
    return row[0] if row else None


def _next_available_ip(conn: sqlite3.Connection, subnet: str) -> str:
    net = ipaddress.ip_network(subnet, strict=True)
    used = {
        ipaddress.ip_address(row[0])
        for row in conn.execute("SELECT assigned_ip FROM peers").fetchall()
    }
    hosts = list(net.hosts())
    if len(hosts) < 3:
        raise ValueError("VPN subnet too small. Use something like 10.66.66.0/24")
    for candidate in hosts[1:]:
        if candidate not in used:
            return str(candidate)
    raise RuntimeError("No available IP addresses in VPN subnet")


@dataclass
class Peer:
    name: str
    private_key: str
    public_key: str
    assigned_ip: str
    active: bool


def cmd_init(args: argparse.Namespace) -> None:
    conn = _init_db()
    _set_setting(conn, "vpn_subnet", args.vpn_subnet)
    _set_setting(conn, "server_public_key", args.server_public_key)
    _set_setting(conn, "server_endpoint", args.endpoint)
    _set_setting(conn, "server_port", str(args.port))
    print("Initialized settings in wg_manager.db")


def cmd_create_peer(args: argparse.Namespace) -> None:
    conn = _init_db()
    vpn_subnet = _get_setting(conn, "vpn_subnet")
    if not vpn_subnet:
        raise RuntimeError("Run init first.")
    assigned_ip = _next_available_ip(conn, vpn_subnet)
    private_key, public_key = _generate_wg_keypair()
    conn.execute(
        "INSERT INTO peers(name, private_key, public_key, assigned_ip, active) VALUES(?, ?, ?, ?, 1)",
        (args.name, private_key, public_key, assigned_ip),
    )
    conn.commit()
    print(f"Created peer '{args.name}' with IP {assigned_ip}")
    print(f"PublicKey: {public_key}")


def _get_peer(conn: sqlite3.Connection, name: str) -> Peer:
    row = conn.execute(
        "SELECT name, private_key, public_key, assigned_ip, active FROM peers WHERE name = ?",
        (name,),
    ).fetchone()
    if not row:
        raise RuntimeError(f"Peer '{name}' not found")
    return Peer(
        name=row[0],
        private_key=row[1],
        public_key=row[2],
        assigned_ip=row[3],
        active=bool(row[4]),
    )


def cmd_revoke_peer(args: argparse.Namespace) -> None:
    conn = _init_db()
    peer = _get_peer(conn, args.name)
    if not peer.active:
        print(f"Peer '{args.name}' is already revoked.")
        return
    conn.execute("UPDATE peers SET active = 0 WHERE name = ?", (args.name,))
    conn.commit()
    print(f"Revoked peer '{args.name}'")


def _allowed_ips(mode: str, vpn_subnet: str, lan_subnet: Optional[str]) -> str:
    if mode == "full":
        return "0.0.0.0/0, ::/0"
    if not lan_subnet:
        raise RuntimeError("split mode requires --lan-subnet")
    return f"{vpn_subnet}, {lan_subnet}"


def cmd_render_client_config(args: argparse.Namespace) -> None:
    conn = _init_db()
    peer = _get_peer(conn, args.name)
    if not peer.active:
        raise RuntimeError(f"Peer '{args.name}' is revoked")
    vpn_subnet = _get_setting(conn, "vpn_subnet")
    server_public_key = _get_setting(conn, "server_public_key")
    endpoint = _get_setting(conn, "server_endpoint")
    port = _get_setting(conn, "server_port") or "51820"
    if not all([vpn_subnet, server_public_key, endpoint]):
        raise RuntimeError("Missing settings; run init first.")
    endpoint_with_port = endpoint if ":" in endpoint else f"{endpoint}:{port}"
    allowed = _allowed_ips(args.mode, vpn_subnet, args.lan_subnet)
    config = f"""[Interface]
PrivateKey = {peer.private_key}
Address = {peer.assigned_ip}/32
DNS = {args.dns}

[Peer]
PublicKey = {server_public_key}
AllowedIPs = {allowed}
Endpoint = {endpoint_with_port}
PersistentKeepalive = 25
"""
    if args.out:
        out_path = Path(args.out)
        out_path.write_text(config, encoding="utf-8")
        print(f"Wrote config to {out_path}")
    else:
        print(config)


def cmd_list_peers(_: argparse.Namespace) -> None:
    conn = _init_db()
    rows = conn.execute(
        "SELECT name, assigned_ip, active FROM peers ORDER BY id ASC"
    ).fetchall()
    if not rows:
        print("No peers created yet.")
        return
    for name, assigned_ip, active in rows:
        state = "active" if active else "revoked"
        print(f"{name:20} {assigned_ip:15} {state}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="WireGuard peer manager (Python MVP)")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_init = sub.add_parser("init", help="Initialize server settings")
    p_init.add_argument("--vpn-subnet", default="10.66.66.0/24")
    p_init.add_argument("--server-public-key", required=True)
    p_init.add_argument("--endpoint", required=True, help="IP or DNS name")
    p_init.add_argument("--port", type=int, default=51820)
    p_init.set_defaults(func=cmd_init)

    p_create = sub.add_parser("create-peer", help="Create a new peer")
    p_create.add_argument("--name", required=True)
    p_create.set_defaults(func=cmd_create_peer)

    p_revoke = sub.add_parser("revoke-peer", help="Revoke a peer")
    p_revoke.add_argument("--name", required=True)
    p_revoke.set_defaults(func=cmd_revoke_peer)

    p_render = sub.add_parser("render-client-config", help="Render client config")
    p_render.add_argument("--name", required=True)
    p_render.add_argument("--dns", default="1.1.1.1")
    p_render.add_argument("--mode", choices=["split", "full"], default="split")
    p_render.add_argument("--lan-subnet", help="Needed in split mode, e.g. 192.168.0.0/24")
    p_render.add_argument("--out", help="Output file path")
    p_render.set_defaults(func=cmd_render_client_config)

    p_list = sub.add_parser("list-peers", help="List peers")
    p_list.set_defaults(func=cmd_list_peers)
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()

