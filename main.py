"""Seventeen Syllables of Debugging — entry program.

Writes one haiku about debugging (three lines, 5-7-5) to entry.txt
in the output directory. Stdlib only, no network, deterministic.
"""

import os

HAIKU = (
    "the duck says nothing\n"
    "I explain the bug out loud\n"
    "and hear the answer\n"
)


def main():
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(HAIKU)
    # Read back and verify the file holds exactly the haiku.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == HAIKU, "entry.txt does not match the haiku"
    assert 1 <= len(written) <= 200, "entry.txt outside the 1-200 char gate"


if __name__ == "__main__":
    main()
