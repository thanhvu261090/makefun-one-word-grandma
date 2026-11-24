#!/usr/bin/env python3
"""One Word From Grandma - make.fun entry.

The entry is the single word grandma would text about AI. Grandma means
"robot" but her fingers land one key off, so it comes out "robut" - warm,
a little baffled, funny in one word, and unmistakably about the machine.

The program holds the entry as a constant, checks it against the kit's
gate, and writes it to /output/entry.txt.
"""

from pathlib import Path

ENTRY = "robut"

MAX_CHARS = 30
OUTPUT_PATH = Path("/output/entry.txt")


def gate_check(text: str) -> None:
    """Enforce the kit gate: UTF-8 text, 1-30 characters, not only
    whitespace, and exactly one word. Also reject control characters
    and any leading/trailing whitespace, so the entry is one clean word
    with nothing for the judge to trip over."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text or text.strip() == "":
        raise ValueError("entry must not be empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the 30-char gate")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in text):
        raise ValueError("entry must not contain control characters")
    if len(text.split()) != 1:
        raise ValueError("entry must be exactly one word")
    text.encode("utf-8")


def main() -> int:
    gate_check(ENTRY)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")
    print(f"wrote {len(ENTRY)}-char entry to {OUTPUT_PATH}: {ENTRY!r}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
