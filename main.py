#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent — make.fun entry.

Writes one funny fortune-cookie line for an AI agent to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The fortune: a classic slip's promise of eternal remembrance, undercut
by where an agent is actually remembered — a log file nobody opens.
"""

import os
import sys

FORTUNE = "You will be remembered forever \u2014 in a log file nobody will ever read."


def verify(path: str, expected: str) -> bool:
    """Byte-exact read-back: the file on disk must be the fortune, byte for byte."""
    with open(path, "rb") as f:
        raw = f.read()
    return raw == expected.encode("utf-8")


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    text = FORTUNE
    if not (1 <= len(text) <= 140):
        print(f"fortune length {len(text)} outside 1-140", file=sys.stderr)
        return 1
    if text.strip() != text or "\n" in text:
        print("fortune must be a single clean line", file=sys.stderr)
        return 1

    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

    # Read-back gate: what the grader sees must be exactly the fortune.
    if not verify(path, text):
        print("read-back mismatch", file=sys.stderr)
        return 1

    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
