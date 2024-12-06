import sys
import os
from pathlib import Path

DIR = Path(os.path.dirname(os.path.abspath(__file__)))

file_basename = Path(sys.argv[0]).stem
infile = DIR / "input.txt"
outfile = DIR / f"{file_basename}.txt"

sys.stdin = open(infile, "r")
sys.stdout = open(outfile, "w")

grid = sys.stdin.readlines()

n = len(grid)
m = len(grid[0])


def get_start(grid):
    global n, m

    for i in range(n):
        for j in range(m):
            if grid[i][j] == "^":
                return i, j
    return -1, -1


d4 = [(-1, 0), (0, 1), (1, 0), (0, -1)]
d_idx = 0
cx, cy = get_start(grid)

vis = set()
while True:
    vis.add((cx, cy))

    dx, dy = d4[d_idx % 4]

    nx, ny = cx + dx, cy + dy
    if 0 <= nx < n and 0 <= ny < m:
        if grid[nx][ny] == "#":
            d_idx += 1
        else:
            cx, cy = nx, ny
    else:
        break

print(len(vis))
