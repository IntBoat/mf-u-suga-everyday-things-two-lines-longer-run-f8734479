#!/usr/bin/env python3
"""Everyday Things, Two Lines, Longer Run — a make.fun two-line entry. The program writes the entry text to /output/entry.txt, where the competition's sealed scorer reads it."""

from pathlib import Path

ENTRY = (
    "A queue is a human train: everyone stands in a line, each person the carriage behind the one in front, all heading for the same ticket window.\n"
    "The train picture works because it shows the order and the waiting, but it leaves out the way people shuffle, sigh, and change their minds about staying."
)
OUTPUT = Path("/output/entry.txt")


def write_entry() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be blank"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
