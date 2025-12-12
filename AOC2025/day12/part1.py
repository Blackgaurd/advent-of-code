import sys
import os
from pathlib import Path
import re

DIR = Path(os.path.dirname(os.path.abspath(__file__)))
infile = DIR / "input.txt"
sys.stdin = open(infile, "r")

input_stream = map(lambda ln: ln.rstrip("\n"), sys.stdin)


class Present:
    def __init__(self, rows: list[list[bool]]):
        self.pieces = 0
        for row in rows:
            for b in row:
                self.pieces += int(b)


def parse_present():
    global input_stream

    rows: list[list[bool]] = []
    for line in input_stream:
        if not line:
            break
        row = [c == "#" for c in line]
        rows.append(row)

    return Present(rows)


def parse_grid(line):
    l, w, *reqs = map(int, re.findall(r"\d+", line))  # noqa: E741
    return l, w, reqs


presents = []
ans = 0
while True:
    try:
        line = next(input_stream)
        if line[1] == ":":
            present = parse_present()
            presents.append(present)
        else:
            l, w, reqs = parse_grid(line)  # noqa: E741

            # this is some bs
            min_fill = sum(p.pieces * r for p, r in zip(presents, reqs))
            if min_fill <= l * w:
                ans += 1
    except StopIteration:
        break

print(ans)
