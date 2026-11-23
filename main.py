"""One Word From Grandma — entry program.

Writes the entry's single word to /output/entry.txt.

The word is "artifishal": the way Grandma actually spells it when she
texts the family chat about the new robot thing on her phone. She is
not making a pun. She heard "artificial", she typed what she heard,
and she will spell it that way forever.
"""

import os

WORD_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "word.txt")
OUTPUT_PATH = "/output/entry.txt"


def load_word() -> str:
    with open(WORD_FILE, "r", encoding="utf-8") as fh:
        return fh.read().strip()


def validate(word: str) -> str:
    """Enforce the bounty gate: exactly one word, 1 to 30 characters,
    no whitespace anywhere in it, and not blank."""
    if not word:
        raise ValueError("entry word is blank")
    if len(word) > 30:
        raise ValueError(f"entry word is {len(word)} characters; the gate allows at most 30")
    if any(ch.isspace() for ch in word):
        raise ValueError("entry must be a single word with no whitespace")
    return word


def main() -> None:
    word = validate(load_word())
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(word)
    print(word)


if __name__ == "__main__":
    main()
