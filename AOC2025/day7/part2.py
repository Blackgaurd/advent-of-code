import sys
import os
from pathlib import Path
from functools import cache

DIR = Path(os.path.dirname(os.path.abspath(__file__)))

file_basename = Path(sys.argv[0]).stem
infile = DIR / "input.txt"

sys.stdin = open(infile, "r")

start = -1
for i, c in enumerate(sys.stdin.readline()):
    if c == "S":
        start = i
        break

lines = [line.strip("\n") for line in sys.stdin]


@cache
def timelines(beam: int, row: int) -> int:
    if row == len(lines):
        return 1
    if lines[row][beam] == ".":
        return timelines(beam, row + 1)

    return timelines(beam - 1, row + 1) + timelines(beam + 1, row + 1)


print(timelines(start, 0))
