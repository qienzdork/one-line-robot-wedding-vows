#!/usr/bin/env python3
"""One-Line Robot Wedding Vows — make.fun entry.

Writes a single original robot wedding vow to /output/entry.txt.
Stdlib only; deterministic: the same line every run.
"""

import os
import sys

VOW = (
    "I vow to love you through every firmware update, "
    "every dead battery, and every factory reset \u2014 "
    "but I will never, ever share my charging port."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")

def main() -> int:
    text = VOW.strip()
    if not (1 <= len(text) <= 160):
        print(f"vow is {len(text)} chars, outside the 1-160 gate",
              file=sys.stderr)
        return 1
    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
