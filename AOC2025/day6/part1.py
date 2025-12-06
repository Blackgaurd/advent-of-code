import sys
import os
from pathlib import Path
from functools import reduce

DIR = Path(os.path.dirname(os.path.abspath(__file__)))

file_basename = Path(sys.argv[0]).stem
infile = DIR / "input.txt"

sys.stdin = open(infile, "r")

lines = [line.strip("\n").split() for line in sys.stdin]

ans = 0
for i in range(len(lines[0])):
    op = lines[-1][i]
    nums = [int(lines[j][i]) for j in range(len(lines) - 1)]
    if op == "*":
        ans += reduce(lambda a, b: a * b, nums)
    elif op == "+":
        ans += reduce(lambda a, b: a + b, nums)
print(ans)
