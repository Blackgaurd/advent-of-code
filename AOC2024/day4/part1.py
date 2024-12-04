import sys
import os
from pathlib import Path
import re

DIR = Path(os.path.dirname(os.path.abspath(__file__)))

file_basename = Path(sys.argv[0]).stem
infile = DIR / "input.txt"
outfile = DIR / f"{file_basename}.txt"

sys.stdin = open(infile, "r")
sys.stdout = open(outfile, "w")


def search(grid, i, j):
    d8 = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, 1), (1, 0), (1, -1)]

    def trace(dx, dy, length=4):
        ret = []
        cx, cy = i, j
        for _ in range(length):
            ret.append(grid[cx][cy])
            cx += dx
            cy += dy

            if cx < 0 or cx >= len(grid):
                break
            if cy < 0 or cy >= len(grid[0]):
                break
        return "".join(ret)

    count = 0
    for dx, dy in d8:
        if trace(dx, dy) == "XMAS":
            count += 1

    return count


grid = sys.stdin.readlines()
count = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        count += search(grid, i, j)
print(count)
