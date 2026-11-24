#!/usr/bin/env python3
# The Robot Vacuum's Best Excuse — make.fun entry.
#
# One line, spoken by the vacuum itself. The program holds the line as a
# plain string, checks it against the competition gate (a single line of
# 1 to 140 characters, nothing but white space forbidden), and only then
# writes it out. If any check fails the program stops without writing.

import sys

LINE = "My dustbin is full of yesterday's spot. I can't eat another crumb until somebody empties me."

LIMIT = 140


def checked_line():
    if "\n" in LINE or "\r" in LINE:
        sys.exit("refusing to write: the entry must be a single line")
    if len(LINE) < 1 or len(LINE) > LIMIT:
        sys.exit("refusing to write: the entry is %d characters, limit %d" % (len(LINE), LIMIT))
    if LINE.strip() == "":
        sys.exit("refusing to write: the entry is only white space")
    if LINE != LINE.strip():
        sys.exit("refusing to write: the entry starts or ends with white space")
    if LINE[-1] not in ".!?":
        sys.exit("refusing to write: the entry does not end with punctuation")
    return LINE


def main():
    text = checked_line()
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text + "\n")
    # Read the file back: a write that silently lands wrong (a partial
    # flush, a different encoding) must fail loudly here, not reach the
    # judge as a different line than the one the gate just approved.
    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != text + "\n":
        sys.exit("refusing to finish: what was written is not the checked line")


if __name__ == "__main__":
    main()
