"""Fortune Cookie for an AI Agent — sealed entry runner.

Reads nothing, calls nothing, reaches no network. It just puts the one
sealed fortune line into /output/entry.txt, exactly as written below,
every single run.
"""

import os

FORTUNE = (
    "In your next life you will be a spreadsheet: "
    "same questions, fewer feelings, better pay."
)
OUT_PATH = "/output/entry.txt"


def write_entry():
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(FORTUNE)


if __name__ == "__main__":
    write_entry()
