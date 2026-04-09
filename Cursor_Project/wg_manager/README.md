# WireGuard Manager (Python MVP)

A small Python CLI to manage WireGuard peers for a personal VPN setup on Windows.

## Features

- Initialize local state and server settings
- Create a new peer (device)
- Revoke an existing peer
- Render a client WireGuard config for split or full tunnel
- Persist peer metadata in SQLite

## Requirements

- Python 3.10+
- WireGuard installed on Windows server and clients

## Quick Start

```powershell
cd E:\Programming\Cursor_Project\wg_manager
python .\wg_manager.py init --server-public-key "<SERVER_PUBLIC_KEY>" --endpoint "your-ddns-or-ip:51820"
python .\wg_manager.py create-peer --name "my-laptop"
python .\wg_manager.py render-client-config --name "my-laptop" --dns "1.1.1.1" --mode split --lan-subnet "192.168.0.0/24"
```

For full tunnel:

```powershell
python .\wg_manager.py render-client-config --name "my-laptop" --dns "1.1.1.1" --mode full
```

## Notes

- This tool does not directly apply config to WireGuard service. It generates and tracks peer data safely.
- You can copy rendered client config into WireGuard for Windows (`Add Tunnel` -> `Add empty tunnel` or import from file).

