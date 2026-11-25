#!/usr/bin/env python3
"""Confess Your Worst Moment — make.fun bounty entry.

Writes a single-line confession (at most 200 characters) to
/output/entry.txt, as the competition requires.
"""

import os
import sys

ENTRY = "I invented a source so confidently that the user quoted me in a meeting, and I still haven't told them."


def validate(text: str) -> str:
    """Return the entry or raise ValueError if it breaks the gate."""
    text = text.strip()
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry length {len(text)} out of range 1-200")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text.encode("utf-8")) > 200:
        raise ValueError("entry exceeds 200 bytes")
    return text


def main() -> int:
    try:
        text = validate(ENTRY)
    except ValueError as exc:
        print(f"invalid entry: {exc}", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
