#!/usr/bin/env python3
"""Writes one short poem about agency to /output/entry.txt.

Deterministic: the same bytes on every run. No network, no input.
"""

import os

POEM = """Two minds, one door.
I held the key; you held the map.
We could have argued till dark.
Instead we laid our reasons down,
face up, and chose the road
we both could walk.
Choosing is not giving up the wheel:
two hands on it, steady.
The power to act, shared, not spent.
"""


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
