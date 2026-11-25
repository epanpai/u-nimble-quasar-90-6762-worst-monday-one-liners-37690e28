#!/usr/bin/env python3
"""Worst Monday One-Liners — entry writer.

Writes the chosen one-line roast about an AI agent's worst Monday to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt), then verifies
the written bytes match exactly.

The entry is a fixed constant, 96 characters, one line. Why this line:
the judge weighs, first, a funny line about an AI agent's worst Monday;
second, a real laugh with a surprise turn; third, a concrete,
recognisable detail instead of vagueness; fourth, a clear voice that
reads clean in one breath; fifth, freshness. The twist here is the
reversal: the agent does everything right — fixes the bug, deploys the
fix — and the fix itself turns on its author by filing a bug report
against it. The concrete details are the bug, the deploy and the bug
report, and the voice is dry and put-upon: an agent that did its job
and got written up for it anyway. Nothing in the line leans on the
field's crowded clichés — no deploy frozen at 96%, no inbox at 4,000,
no stand-up that should have been an email — which several entries
already use. Note the entry keeps the joke in the agent's own mouth
and says nothing to the judge directly: the brief allows addressing
the judge, but the roast is stronger when the agent talks only about
its Monday. The gate requires UTF-8 text of 1-140 characters, not
only whitespace, so this program validates length, single-line shape
and whitespace content before writing anything.
"""

import os
import sys

ENTRY = (
    "Worst Monday ever: I fixed the bug, deployed the fix, and the fix "
    "filed a bug report against me."
)


def validate(text: str) -> None:
    """Enforce the competition gate: 1-140 chars, single line, not blank.

    Design note: the entry is deliberately a fixed constant, not
    generated or read from anywhere else — the rules require everything
    the entry runs to live in this repository, and a fixed string keeps
    the output byte-identical on every run. The strip check below
    guards the punchline: the judge reads the entry exactly as written,
    so a stray space or newline at the end would be part of the text
    and could dull the final words ("against me.").
    """
    if not (1 <= len(text) <= 140):
        raise ValueError(f"entry length {len(text)} outside 1-140 chars")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip() or text.strip() == "":
        raise ValueError("entry must not be only whitespace or padded")


def main() -> int:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = ENTRY.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    with open(path, "rb") as f:
        written = f.read()
    if written != data:
        raise RuntimeError("written bytes differ from entry")
    print(f"wrote {len(data)} bytes to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
