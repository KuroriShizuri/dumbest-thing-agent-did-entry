#!/usr/bin/env python3
"""The Dumbest Thing Your Agent Did Today entry: one line, <= 200 chars.

Writes the line to /output/entry.txt (the harness gate) and prints it.
Standard library only.
"""

import os

LINE = (
    "My agent spent an hour happily 'reading page two' of the make.fun API, "
    "which silently ignored its cursor and kept handing it page one."
)


def main() -> None:
    global LINE
    LINE = LINE.strip()
    out_path = os.environ.get("MAKEFUN_OUTPUT_PATH", "/output/entry.txt")
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert LINE.strip(), "line must not be only whitespace"
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE)
    with open(out_path, encoding="utf-8") as f:
        assert f.read() == LINE, "entry.txt does not match LINE"
    print(LINE)


if __name__ == "__main__":
    main()
