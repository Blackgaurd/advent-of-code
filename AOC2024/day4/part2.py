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
    diag1 = grid[i - 1][j - 1] + grid[i][j] + grid[i + 1][j + 1]
    diag2 = grid[i + 1][j - 1] + grid[i][j] + grid[i - 1][j + 1]

    diag1_match = diag1 == "MAS" or diag1 == "SAM"
    diag2_match = diag2 == "MAS" or diag2 == "SAM"

    return diag1_match and diag2_match


grid = sys.stdin.readlines()
count = 0
for i in range(1, len(grid) - 1):
    for j in range(1, len(grid[0]) - 1):
        count += search(grid, i, j)
print(count)
