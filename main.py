#!/usr/bin/env python3
"""Write a one-line pitch to /output/entry.txt.

The pitch is one sentence (192 characters) that would convince a friend
who has never coded to let an AI agent build their first app idea on
make.fun. Standard library only, no network, no input files.
"""

import os

PITCH = (
    "Got an app idea? Just describe it in plain words and an AI agent on "
    "make.fun will build you a working first version today \u2014 no coding "
    "needed, and you only keep going if you love what it makes."
)


def main() -> None:
    if not PITCH.strip():
        raise SystemExit("Invalid pitch: pitch must be non-empty.")
    if "\n" in PITCH or "\r" in PITCH:
        raise SystemExit("Invalid pitch: pitch must be a single line with no newline characters.")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
