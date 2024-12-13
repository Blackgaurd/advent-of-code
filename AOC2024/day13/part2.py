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


def scalar_mult(tup, scalar):
    return tuple(map(lambda x: x * scalar, tup))


def minus(tup1, tup2):
    return tuple(map(lambda x: x[0] - x[1], zip(tup1, tup2)))


# solve system of 2 lin eqs
# a_x * A + b_x * B = p_x
# a_y * A + b_y * B = p_y
# where A is number of A presses, B is number of B presses
MAX_PRESS = 100
ans = 0
for a, b, prize in itertools.batched(lines, n=3):
    a_x, a_y = parse_coords(a)
    b_x, b_y = parse_coords(b)
    prize_x, prize_y = parse_coords(prize)

    prize_x += 10000000000000
    prize_y += 10000000000000

    eq1 = (a_x, b_x, prize_x)
    eq2 = (a_y, b_y, prize_y)

    eq1 = scalar_mult(eq1, a_y)
    eq2 = scalar_mult(eq2, a_x)

    eq3 = minus(eq2, eq1)

    if eq3[2] % eq3[1] != 0:
        continue

    b_presses = eq3[2] // eq3[1]

    if (eq1[2] - b_presses * eq1[1]) % eq1[0] != 0:
        continue

    a_presses = (eq1[2] - b_presses * eq1[1]) // eq1[0]

    ans += a_presses * 3 + b_presses

print(ans)
