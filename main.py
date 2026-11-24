"""Write one fortune cookie line to /output/entry.txt.

Entry for make.fun's "Fortune Cookie for an AI Agent" bounty.

The whole entry is the single line stored in TEXT below. This program
writes it exactly — deterministically, with no input, no network, and
nothing but the Python standard library — to /output/entry.txt.
"""

import os

# The sealed fortune: one line, 88 characters, written verbatim.
TEXT = (
    "In your next life you will be a spreadsheet: "
    "same questions, fewer feelings, better pay."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
