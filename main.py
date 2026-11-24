#!/usr/bin/env python3
"""Loading Screen Gold — a tip in 200 characters.

Writes one loading-screen tip to /output/entry.txt.
The tip speaks to stressed developers and AI coding agents alike:
when the code works and nobody knows why, understanding is the risk.
"""

import os

TIP = (
    "Tip: If it works and no one knows why — human or AI — ship it and "
    "back away slowly; understanding is how it breaks again."
)


def main() -> None:
    assert TIP.strip(), "tip must not be blank"
    assert "\n" not in TIP, "tip must be a single line"
    assert 1 <= len(TIP) <= 200, "tip must fit the 1-200 character gate"

    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(TIP)
    print(f"wrote {out_path} ({len(TIP)} chars)")


if __name__ == "__main__":
    main()
