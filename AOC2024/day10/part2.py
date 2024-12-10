from re import L
import sys
import os
from pathlib import Path
from collections import deque

DIR = Path(os.path.dirname(os.path.abspath(__file__)))

file_basename = Path(sys.argv[0]).stem
infile = DIR / "input.txt"
outfile = DIR / f"{file_basename}.txt"

sys.stdin = open(infile, "r")
sys.stdout = open(outfile, "w")

grid = []
for line in sys.stdin.readlines():
    line = line.rstrip("\n")
    grid.append(line)


d4 = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def score(grid, sx, sy):
    if grid[sx][sy] == "9":
        return 1

    ans = 0
    for dx, dy in d4:
        nx, ny = sx + dx, sy + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            if int(grid[nx][ny]) == int(grid[sx][sy]) + 1:
                ans += score(grid, nx, ny)
    return ans


ttl = 0
for i, row in enumerate(grid):
    for j, x in enumerate(row):
        if x == "0":
            ttl += score(grid, i, j)
print(ttl)
