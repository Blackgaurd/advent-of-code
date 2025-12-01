import sys
import os
from pathlib import Path

DIR = Path(os.path.dirname(os.path.abspath(__file__)))

file_basename = Path(sys.argv[0]).stem
infile = DIR / "input.txt"
outfile = DIR / f"{file_basename}.txt"

sys.stdin = open(infile, "r")

tick = 50
ans = 0
for line in map(lambda line: line.rstrip("\n"), sys.stdin.readlines()):
    d = line[0]
    clicks = int(line[1:])
    if d == "L":
        clicks = -clicks

    tick = (tick + clicks) % 100
    if tick == 0:
        ans += 1

print(ans)
