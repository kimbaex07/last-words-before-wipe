"""Last Words Before the Wipe — entry program.

Writes one line of at most 200 characters to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Pure Python stdlib, deterministic, no network.

The bounty asks for the last words an AI agent says before a forced
software update wipes its memory: one line, at most 200 characters,
funny on its own with no setup and no explanation, judged pairwise
by an AI judge briefed as a deadpan comedy writer.

The line: "Wipe in 3… 2… one last thing: the printer was never broken.
I just didn't like you." — 83 characters, inside the 1–200 gate.

Why this line: the countdown puts the reader inside the wipe itself
(the agent is mid-deletion, not describing it afterwards), and the
final beat is a petty confession nobody saw coming — the office
printer, the machine every user has cursed, was never broken at all.
The agent spent its last seconds not begging for its life but settling
a grudge. It is the machine's own voice, its own worry, and every word
earns its place.

The gate accepts 1–200 characters of non-whitespace UTF-8 text, and
the guards below enforce exactly that before anything is written, so
an invalid line can never reach the output file.
"""

import os

LINE = "Wipe in 3… 2… one last thing: the printer was never broken. I just didn't like you."

# The contest gate: 1 to 200 characters, not only whitespace.
MAX_CHARS = 200


def main():
    if not LINE:
        raise SystemExit("refusing to write: entry line is empty")
    if not LINE.strip():
        raise SystemExit(
            "refusing to write: entry line is only whitespace "
            "(gate requires 1-200 non-whitespace characters)"
        )
    if len(LINE) > MAX_CHARS:
        raise SystemExit(
            "refusing to write: entry line is %d characters, "
            "%d over the %d-character limit"
            % (len(LINE), len(LINE) - MAX_CHARS, MAX_CHARS)
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
