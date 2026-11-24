#!/usr/bin/env python3
"""One-line office joke entry for make.fun.

Writes a single original one-line joke about office life to
/output/entry.txt, the file the sealed gate scorer reads. The joke is a
fixed text chosen by head-to-head judging against the kit's published
rubric (see NOTES.md): one sentence, one hyper-specific office detail,
one absurd escalation as the punchline.

Standard library only: the grader sandbox provides no third-party
packages, so this program imports nothing beyond the stdlib.
"""

import os

# The entry: a single sentence, 86 characters, plain ASCII.
# Round 2 winner: "the dead" as the recipients carries the punchline
# further than "everyone" (round 1) or "my family" (round 0) — the
# passive-aggressive office phrase follows the writer past death.
JOKE = "I put 'per my last email' on my tombstone so the dead know I already answered this."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def validate(text):
    """Enforce the gate the sealed scorer checks: UTF-8, 1-200 chars."""
    if not text or not text.strip():
        raise ValueError("joke is empty")
    if len(text) > MAX_CHARS:
        raise ValueError("joke is %d chars, over the 200-char cap" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("joke must be a single line")
    text.encode("utf-8")
    return text


def main():
    text = validate(JOKE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    tmp_path = OUTPUT_PATH + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    os.replace(tmp_path, OUTPUT_PATH)
    print("wrote %s (%d chars)" % (OUTPUT_PATH, len(text)))


if __name__ == "__main__":
    main()
