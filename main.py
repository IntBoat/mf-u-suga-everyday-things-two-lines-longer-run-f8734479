#!/usr/bin/env python3
"""Everyday Things, Two Lines, Longer Run (make.fun).

Writes the entry -- two lines explaining an everyday thing (a toaster) to a
10-year-old, analogy plus what the analogy leaves out --
to /output/entry.txt, where the sealed scorer reads it."""

import os

TEXT = 'A toaster is a tiny sun-tanning bed for bread: it lies flat, soaks up the heat, and pops up golden-brown when its timer rings.\nThe tanning-bed picture fits the heat and the pop-up, but it leaves out that bread cannot choose its tan — the dial does.'


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
