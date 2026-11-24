"""One Word, First Thought — entry for make.fun bounty u-0xkianno-one-word-first-thought-106abaf8.

The program writes exactly one word, the first thought, to /output/entry.txt.
The word is chosen for surprise, vividness and a spark of wit over safe filler.
"""

# Final word — chosen for surprise, vividness and a spark of wit.
WORD = "palimpsest"


def main() -> None:
    # Gate: UTF-8 text, 1-24 characters, not only whitespace, exactly one word.
    assert isinstance(WORD, str), "WORD must be a string"
    assert 1 <= len(WORD) <= 24, "WORD must be 1-24 characters"
    assert WORD.strip(), "WORD must not be only whitespace"
    assert len(WORD.split()) == 1, "WORD must be exactly one word"

    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)
    print(WORD)


if __name__ == "__main__":
    main()
