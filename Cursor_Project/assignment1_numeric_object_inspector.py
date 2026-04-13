#!/usr/bin/env python3
"""
Assignment 1 – Numeric & Object Inspector
Practice: variables, types, conversion, object identity, and exception handling.
"""

from __future__ import annotations


def read_int(prompt: str) -> int:
    """
    Read a base-10 integer from the user.
    Invalid text is rejected with a clear message (exception handling).
    """
    while True:
        raw = input(prompt).strip()
        try:
            # int() converts a string to int; ValueError if not a valid integer literal
            return int(raw)
        except ValueError:
            print(
                f"  -> Could not parse {raw!r} as an integer. "
                "Try a whole number like -12, 0, or 99."
            )


def read_float(prompt: str) -> float:
    """Read a floating-point number; retry on invalid input."""
    while True:
        raw = input(prompt).strip()
        try:
            # float() converts numeric text; ValueError if the string is not a float literal
            return float(raw)
        except ValueError:
            print(
                f"  -> Could not parse {raw!r} as a float. "
                "Try values like 3.14, -0.5, 2, or 1e3."
            )


def read_string(prompt: str) -> str:
    """Any user text is accepted as a string (including empty string)."""
    return input(prompt)


def report_type_and_id(label: str, value: object) -> None:
    """Print runtime type and object identity for one variable."""
    print(f"  {label}")
    print(f"    type(value) -> {type(value)}")
    print(f"    id(value)   -> {id(value)}")


def string_converts_to_int_safely(text: str) -> bool:
    """
    Return True if int(text) would succeed for base-10 integers.
    Uses exception handling instead of guessing with string methods
    (handles signs, leading zeros edge cases consistently).
    """
    try:
        int(text.strip())
        return True
    except ValueError:
        return False


def main() -> None:
    print("Numeric & Object Inspector")
    print("-" * 40)

    # --- Step 1: prompt for an integer, a float, and a string ---
    print("\n[Step 1] Enter three values\n")
    user_int = read_int("  Integer: ")
    user_float = read_float("  Float:   ")
    user_string = read_string("  String:  ")

    # --- Step 2: show type() and id() for each variable ---
    print("\n[Step 2] type() and id() for each variable\n")
    report_type_and_id("Integer variable:", user_int)
    report_type_and_id("Float variable:", user_float)
    report_type_and_id("String variable:", user_string)

    # --- Step 3: integer → binary via bin(); show bit length ---
    print("\n[Step 3] Integer as binary and its bit length\n")
    # bin() returns a string with a '0b' prefix representing the value in base 2
    binary_form = bin(user_int)
    # bit_length(): number of bits required to represent abs(n) in binary, excluding sign
    # Special case: (0).bit_length() is 0
    bits = user_int.bit_length()
    print(f"  bin(integer)              -> {binary_form}")
    print(f"  integer.bit_length()      -> {bits} bits")

    # --- Step 4: explicit float → int (truncates toward zero) ---
    print("\n[Step 4] Explicit conversion: float -> int\n")
    try:
        # int() from float truncates toward zero (not “round”)
        float_as_int = int(user_float)
        print(f"  int(float_value)          -> {float_as_int}")
    except (ValueError, OverflowError) as exc:
        # NaN cannot convert to int (ValueError); infinities raise OverflowError
        print(f"  int(float_value) failed:   {type(exc).__name__}: {exc}")

    # Satisfy explicit use of float() on a non-input value (demonstrates conversion API)
    print(f"  float(integer) for contrast -> {float(user_int)}")

    # --- Step 5: can the string be turned into an integer safely? ---
    print("\n[Step 5] String -> integer safety check\n")
    if string_converts_to_int_safely(user_string):
        try:
            parsed = int(user_string.strip())
            print(f"  Safe: int(string) -> {parsed}")
        except ValueError:
            # Defensive: should not happen if string_converts_to_int_safely was True
            print("  Unexpected: conversion failed after safety check.")
    else:
        print(
            f"  Not safe: {user_string!r} cannot be parsed as a base-10 integer "
            "without error."
        )

    # --- Step 6: Boolean (“truthiness”) of each stored value ---
    print("\n[Step 6] Boolean evaluation of each input-derived value\n")
    print(f"  bool(integer) -> {bool(user_int)}  (False only if integer is 0)")
    print(f"  bool(float)   -> {bool(user_float)}  (False only if float is 0.0)")
    print(f"  bool(string)  -> {bool(user_string)}  (False for empty string)")


if __name__ == "__main__":
    main()
