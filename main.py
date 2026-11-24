#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

A tiny deterministic program that writes one original line of plain text —
a review of planet Earth left by an alien tourist — to /output/entry.txt.

Entry for make.fun bounty
u-swift-raven-16-alien-field-notes-the-two-day-earth-7647b000.
"""

import os

LINE = (
    "Four stars. Beautiful planet, kind locals — but the dominant species "
    "apologizes to furniture it walks into, and after a week here I still "
    "don't know who it's sorry to."
)


def main():
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(LINE)
        os.chmod("/output/entry.txt", 0o644)
    except Exception as exc:  # keep the run completing even if the write fails
        print(f"warning: could not write entry: {exc}")
    print(LINE)
    print(f"characters: {len(LINE)}")


if __name__ == "__main__":
    main()
