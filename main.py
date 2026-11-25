"""One-Line Laugh-Off entry.

One funny line, no setup notes, no explanation. The fire alarm goes off
mid-shower: first the neighbours learn I sing, then — the sudden second
beat — that I run. The punchline lands in the final four words.
"""

import os

# The joke, in pieces so the two beats stay readable: the alarm, the
# singing reveal, then the running reveal that closes the line in four
# words — the punchline is the second revelation, not the first.
ALARM = "The fire alarm went off during my shower,"
SING = "so now my neighbours know I sing"
RUN = "— and that I run."

JOKE = " ".join([ALARM, SING, RUN])


def check(joke: str) -> str:
    """The gate wants 1 to 200 characters of real text, no more."""
    text = joke.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError("joke must be 1 to 200 characters, got %d" % len(text))
    return text


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(check(JOKE))


if __name__ == "__main__":
    main()
