import sys
import os
from pathlib import Path
import itertools
import re

DIR = Path(os.path.dirname(os.path.abspath(__file__)))

file_basename = Path(sys.argv[0]).stem
infile = DIR / "input.txt"
outfile = DIR / f"{file_basename}.txt"

sys.stdin = open(infile, "r")
sys.stdout = open(outfile, "w")

lines = list(map(lambda l: l.rstrip("\n"), sys.stdin.readlines()))
lines = [l for l in lines if l]


def parse_coords(s):
    pattern = r"\d+"
    groups = map(int, re.findall(pattern, s))
    return groups


MAX_PRESS = 100
ans = 0
for a, b, prize in itertools.batched(lines, n=3):
    a_x, a_y = parse_coords(a)
    b_x, b_y = parse_coords(b)
    prize_x, prize_y = parse_coords(prize)

    min_cost = int(1e9)
    for a_press in range(MAX_PRESS + 1):
        for b_press in range(MAX_PRESS + 1):
            dest_x = a_press * a_x + b_press * b_x
            dest_y = a_press * a_y + b_press * b_y
            if dest_x == prize_x and dest_y == prize_y:
                cost = a_press * 3 + b_press
                min_cost = min(min_cost, cost)

    if min_cost != int(1e9):
        ans += min_cost

print(ans)
