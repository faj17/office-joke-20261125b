"""One-line office joke for the make.fun bounty.

The whole entry is a single sentence: a meeting that could have been
an email, with the twist that the email would have needed a meeting
of its own to explain it. The script validates the line and drops it
into /output/entry.txt.
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
    """Strip and sanity-check the joke; raise ValueError on bad input."""
    text = line.strip()
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"joke must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(text)}"
        )
    if "\n" in text:
        raise ValueError("joke must be a single line")
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
