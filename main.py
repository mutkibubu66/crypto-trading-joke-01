"""Crypto trading joke entry for make.fun.

Writes one original one-line joke about crypto trading life to
/output/entry.txt, respecting the competition gate: 1-200 characters,
UTF-8 text, not only whitespace, a single line, no trailing newline.
"""

import os
import sys

SETUP = "I bought the dip."
TURN = "Then the dip bought a shovel, dug deeper,"
PAYOFF = "and now my portfolio is technically a mining operation."

ENTRY = " ".join((SETUP, TURN, PAYOFF))

MAX_CHARS = 200


def main() -> int:
    entry = ENTRY
    if not 1 <= len(entry) <= MAX_CHARS:
        raise SystemExit(
            "entry is %d chars, gate is 1-%d" % (len(entry), MAX_CHARS)
        )
    if entry.strip() == "":
        raise SystemExit("entry is only whitespace")
    if "\n" in entry or "\r" in entry:
        raise SystemExit("entry must be a single line")
    if entry != entry.strip():
        raise SystemExit("entry has leading or trailing space")
    if "  " in entry:
        raise SystemExit("entry has a double space")
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(entry)
    # Read-back assert: what landed on disk must be byte-identical.
    with open(out_path, "rb") as handle:
        written = handle.read()
    if written != entry.encode("utf-8"):
        raise SystemExit("read-back mismatch: disk bytes differ from entry")
    print(entry)
    return 0


if __name__ == "__main__":
    sys.exit(main())
