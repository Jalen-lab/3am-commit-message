#!/usr/bin/env python3
"""The 3AM Commit Message.

The bounty asks for one line, at most 139 characters: the funniest git
commit message an AI coding agent might type at 3am after a long night
of fixing its own bugs. A model judge compares entries two at a time on
the brief sealed with the bounty. The brief weighs, in order: the line
reads as a one-line commit message from that exhausted agent; it is the
funnier of the two, the laugh landing on the first read from the
situation alone; it feels fresh rather than recycled; it sounds like a
real commit line typed in a hurry by something awake too long, not a
polished slogan; and it uses its characters well, no padding.

The line this program writes is:

    fix: removed the bug I introduced at 2am fixing the bug I
    introduced at 1am. the tests pass. I no longer trust the tests

Why it is built that way: the first half is the night itself in one
breath, a loop where every fix plants the next bug, and the loop is the
joke an agent that debugs its own code would actually live through.
The second half is the punchline the loop earns: the tests pass, which
after a night like that is not reassuring, it is suspicious, so the
agent trusts the green checkmarks less than the bugs. It reads like a
real commit because it starts with "fix:", stays flat and tired, and
never explains itself. It is 120 characters, inside the 139 limit, and
every clause carries the joke forward.

The program does one thing and does it the same way every run: it writes
exactly that line, and nothing else, to entry.txt in the output
directory.
"""

import os

MESSAGE = (
    "fix: removed the bug I introduced at 2am fixing the bug I "
    "introduced at 1am. the tests pass. I no longer trust the tests"
)


def main() -> None:
    if not 1 <= len(MESSAGE) <= 139:
        raise ValueError(f"commit message must be 1-139 characters, got {len(MESSAGE)}")
    if "\n" in MESSAGE or "\r" in MESSAGE:
        raise ValueError("commit message must be a single line")
    if not MESSAGE.strip():
        raise ValueError("commit message must not be only whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(MESSAGE)
    os.chmod(path, 0o644)
    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != MESSAGE:
        raise ValueError("entry.txt does not match the commit message after writing")
    print(MESSAGE)


if __name__ == "__main__":
    main()
