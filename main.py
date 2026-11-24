#!/usr/bin/env python3
"""Writes one line to /output/entry.txt: a one-star review by a house cat.

Deterministic, offline, no randomness, no network. The whole deliverable is
the LINE constant below; the rest of the file only places it on disk.
"""

from __future__ import annotations

import os
from pathlib import Path

LINE = (
    "One star. Left him a warm mouse on the rug, plated the way he plates "
    "dinner. He screamed and fetched the broom. I have never once screamed "
    "at the cold dead chicken he buys in a bag."
)


def output_path() -> Path:
    """$MAKEFUN_OUTPUT_DIR/entry.txt when set, else /output/entry.txt."""
    override = os.getenv("MAKEFUN_OUTPUT_DIR")
    base = Path(override) if override else Path("/output")
    return base / "entry.txt"


def main() -> int:
    text = LINE.strip()
    if not text:
        raise SystemExit("refusing to write an empty entry")
    if len(text) > 200:
        raise SystemExit(f"entry is {len(text)} code points, over the 200 limit")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")

    path = output_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    # newline="" stops Python translating "\n" and appending anything: the
    # file holds exactly the characters of LINE, with no trailing newline.
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)

    print(f"wrote {len(text)} code points to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
