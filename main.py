"""The Houseplant Out-of-Office — make.fun entry.

Writes one out-of-office auto-reply, as if a houseplant had written it,
to /output/entry.txt. Deterministic: no network, no randomness, no input.
"""

import os
from pathlib import Path

LINE = (
    "Out of office: I've sat in this corner since March, "
    "unwatered and unbothered. Your email can wait. "
    "I've waited longer."
)


def main() -> None:
    # The gate requires 1-120 characters of UTF-8 text, not only whitespace.
    assert 1 <= len(LINE) <= 120, f"line is {len(LINE)} chars"
    assert LINE.strip(), "line must not be only whitespace"
    output = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
