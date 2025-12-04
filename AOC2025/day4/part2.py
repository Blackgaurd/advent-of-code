import sys
import os
from pathlib import Path
from itertools import product
from copy import deepcopy

DIR = Path(os.path.dirname(os.path.abspath(__file__)))

file_basename = Path(sys.argv[0]).stem
infile = DIR / "input.txt"

sys.stdin = open(infile, "r")

grid = [list(line.rstrip("\n")) for line in sys.stdin.readlines()]


def remove(grid: list[list[str]]):
    new_grid = deepcopy(grid)

    ans = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != "@":
                continue

            count = 0
            for dx, dy in product((-1, 0, 1), (-1, 0, 1)):
                ni = i + dx
                nj = j + dy
                if ni < 0 or ni >= len(grid):
                    continue
                if nj < 0 or nj >= len(grid[0]):
                    continue
                if grid[ni][nj] == "@":
                    count += 1

            if count - 1 < 4:
                ans += 1
                new_grid[i][j] = "."

    return new_grid, ans


tot_removed = 0
while True:
    grid, removed = remove(grid)
    tot_removed += removed
    if removed == 0:
        break

print(tot_removed)
