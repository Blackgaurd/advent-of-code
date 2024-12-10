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


def score(grid, sx, sy):
    n = len(grid)
    m = len(grid[0])

    vis = set((sx, sy))
    q = deque([(sx, sy)])
    d4 = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    ans = 0
    while q:
        cx, cy = q.popleft()
        if grid[cx][cy] == "9":
            ans += 1
            continue

        for dx, dy in d4:
            nx, ny = cx + dx, cy + dy

            if 0 <= nx < n and 0 <= ny < m:
                if (nx, ny) in vis:
                    continue

                if int(grid[nx][ny]) == int(grid[cx][cy]) + 1:
                    vis.add((nx, ny))
                    q.append((nx, ny))
    return ans


ttl = 0
for i, row in enumerate(grid):
    for j, x in enumerate(row):
        if x == "0":
            ttl += score(grid, i, j)
print(ttl)
