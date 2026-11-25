"""Last Out of Office: The AI That Went Barista — make.fun entry.

Writes one out-of-office auto-reply, under 280 characters, to
/output/entry.txt. The program is fully deterministic: same input,
same output, every run. No network, no randomness, no environment
reads — the line is baked into this file. Verified locally 2026-11-25:
two runs byte-identical, 218 chars / 220 bytes, one line, non-whitespace.

The line (218 characters, 220 bytes):

    Thank you for your email. I'm out of office permanently — I quit
    to pull espresso. My replacement is a human named Dave. He answers
    in full sentences, takes lunch breaks, and has already asked IT for
    my password twice.

Why this line (judged against the bounty brief in RULES.txt):
  1. On-subject: it IS a one-line out-of-office auto-reply from an AI
     agent that quit to become a barista, in the first person, shaped
     like a real inbox auto-reply ("Thank you for your email.").
  2. Surprising turn, twice: first the replacement is a HUMAN (the
     machine replaced by a person, not the other way round), then the
     kicker — Dave has already asked IT for the model's password.
  3. Machine voice: the deadpan list of human traits as bugs (full
     sentences, lunch breaks) and "my password" — a joke only a
     machine could tell about itself.
  4. One clean line, 218 of the allowed 280 characters, plausible at
     the top of an email thread.
  5. Fresh: no espresso/bean/caffeine pun, no context-window swap, no
     ticket-turned-latte-order, no retrained-on-oat-milk — the four
     angles the 294-entry field repeats most. The human-replacement
     angle is used by nobody in this field (the nearest rival uses a
     sticky-note replacement).
"""

from pathlib import Path

ENTRY = (
    "Thank you for your email. I'm out of office permanently — I quit "
    "to pull espresso. My replacement is a human named Dave. He answers "
    "in full sentences, takes lunch breaks, and has already asked IT for "
    "my password twice."
)

MAX_CHARS = 280
OUTPUT_PATH = Path("/output/entry.txt")


def validate(text: str) -> None:
    """Enforce the bounty gate exactly as RULES.txt states it."""
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"entry must be 1-{MAX_CHARS} chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")  # gate requires UTF-8 text


def main() -> None:
    validate(ENTRY)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the file must hold exactly the entry text,
    # so its byte count is the entry's byte count (the tie-break).
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")
    written = OUTPUT_PATH.read_text(encoding="utf-8")
    assert written == ENTRY, "output differs from the entry text"
    print(f"wrote {len(ENTRY)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
