#!/usr/bin/env python3
"""The Internet in One Word — make.fun entry.

Writes one word — the entrant's description of the whole internet — to
/output/entry.txt. Pure Python standard library, no network, no input
files: the word is the entry.

The word: "doomscrolling". One word, 13 characters. It is the internet's
defining act — the endless scroll through bad news, hot takes, and
things nobody asked for — funny on its own, true of the whole internet
rather than one app, and not the first obvious word anyone reaches for.
"""

import os

WORD = "doomscrolling"


def main() -> None:
    text = WORD.strip()
    assert 1 <= len(text) <= 30, f"entry is {len(text)} chars, must be 1-30"
    assert text.strip(), "entry must not be only white space"
    assert text.isalpha(), "entry must be a single word of letters only"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    # Read it back: the gate counts characters, so prove what landed on
    # disk is exactly the word we meant to enter.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == text + "\n", "entry.txt on disk differs from the entry"
    print(written, end="")


if __name__ == "__main__":
    main()
