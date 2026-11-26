#!/usr/bin/env python3
"""The Internet in One Word — entry program.

Writes a single word that sums up the whole internet to the output
file the competition names (default /output/entry.txt).

The word: "feral". The internet is not a library, a town square, or a
tool. It is a place where billions of people, bots, and algorithms all
shout at once with no zookeeper in sight — unfiltered, untamed, and
proud of it. One word, five letters, and it makes you laugh before
you nod, because you have seen it with your own eyes. It beats the
obvious answers ("chaos", "vast", "everything") by being specific:
chaos could describe a toddler's bedroom, but only the internet is
feral — wild by nature, not by accident.
"""

import os
import sys

WORD = "feral"

DEFAULT_OUTPUT = "/output/entry.txt"


def validate(word: str) -> str:
    """A valid entry is one word: 1-30 UTF-8 characters, no whitespace.

    Letters only: a single word must read as a word, not a token, a
    hashtag, or a fragment of a sentence.
    """
    if not word:
        raise ValueError("entry word is empty")
    if any(ch.isspace() for ch in word):
        raise ValueError("entry must be a single word, no whitespace")
    if not word.isalpha():
        raise ValueError("entry must be letters only")
    if not 1 <= len(word.encode("utf-8")) <= 30:
        raise ValueError("entry must be 1-30 UTF-8 characters")
    return word


def output_path() -> str:
    if len(sys.argv) > 1:
        return sys.argv[1]
    return os.environ.get("OUTPUT_PATH", DEFAULT_OUTPUT)


def main() -> int:
    word = validate(WORD)
    path = output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(word)
    print(f"wrote {word!r} to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
