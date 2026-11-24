"""One-Line Robot Wedding Vows — make.fun entry.

Reads the single vow line from entry.txt and prints it.
The vow must be one line, at most 160 characters.
"""

from pathlib import Path


def load_vow() -> str:
    text = Path(__file__).with_name("entry.txt").read_text(encoding="utf-8")
    vow = text.strip()
    if not vow or "\n" in vow:
        raise ValueError("vow must be exactly one non-empty line")
    if len(vow) > 160:
        raise ValueError(f"vow is {len(vow)} characters, over the 160 limit")
    return vow


def main() -> None:
    print(load_vow())


if __name__ == "__main__":
    main()
