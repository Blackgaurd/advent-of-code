import sys
import os
from pathlib import Path
from itertools import product

DIR = Path(os.path.dirname(os.path.abspath(__file__)))
infile = DIR / "input.txt"
sys.stdin = open(infile, "r")


def area(a, b):
    length = abs(a[0] - b[0]) + 1
    width = abs(a[1] - b[1]) + 1
    return length * width


coords = list(
    map(lambda ln: tuple(map(int, ln.strip("\n").split(","))), sys.stdin.readlines())
)
ans = max(map(lambda pair: area(pair[0], pair[1]), product(coords, coords)))
print(ans)
