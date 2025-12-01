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
    d = -1 if line[0] == "L" else 1
    clicks = int(line[1:])

    for _ in range(clicks):
        tick += d
        tick %= 100
        if tick == 0:
            ans += 1

print(ans)
