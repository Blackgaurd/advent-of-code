import sys
import os
from pathlib import Path
from itertools import combinations

DIR = Path(os.path.dirname(os.path.abspath(__file__)))

file_basename = Path(sys.argv[0]).stem
infile = DIR / "input.txt"
outfile = DIR / f"{file_basename}.txt"

sys.stdin = open(infile, "r")
sys.stdout = open(outfile, "w")

pairs = set()
computers = set()

for line in map(lambda s: s.strip("\n"), sys.stdin):
    x, y = line.split("-")
    computers.add(x)
    computers.add(y)

    if x > y:
        x, y = y, x
    pairs.add((x, y))


ans = 0
for a, b, c in combinations(computers, 3):
    a, b, c = sorted((a, b, c))
    if (a, b) in pairs and (b, c) in pairs and (a, c) in pairs:
        if a.startswith("t") or b.startswith("t") or c.startswith("t"):
            ans += 1

print(ans)
