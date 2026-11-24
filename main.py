"""One-line office joke for the make.fun bounty.

The whole entry is a single sentence: a meeting that could have been
an email, with the twist that the email would have needed a meeting
of its own to explain it. The script validates the line and drops it
into /output/entry.txt.

Gate: 1-200 chars, exactly one line, one sentence, ends with a full stop.
No leading or trailing whitespace; no newline or carriage return anywhere.
"""

from pathlib import Path

# The joke itself: one sentence, exactly 94 characters.
JOKE = (
    "Our meeting could have been an email, but the email would have "
    "needed a meeting to explain it."
)

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"
MIN_CHARS = 1
MAX_CHARS = 200


def validate(line: str) -> str:
    """Sanity-check the joke; raise ValueError on bad input.

    The entry must be exactly one line: no newline or carriage return
    anywhere in it, and no leading or trailing whitespace. Input is
    checked as given, not silently stripped, so a bad line fails loudly
    instead of being quietly fixed.
    """
    if line != line.strip():
        raise ValueError("joke must have no leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("joke must be a single line (no newline)")
    text = line
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"joke must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(text)}"
        )
    if not text.endswith("."):
        raise ValueError("joke must end with a full stop")
    if ". " in text:
        raise ValueError("joke must be a single sentence (no '. ' inside)")
    return text


def main() -> None:
    text = validate(JOKE)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(text, encoding="utf-8")
    print(text)
    print(f"Wrote {len(text)} chars to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
