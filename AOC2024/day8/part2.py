import sys
import os
from pathlib import Path
from collections import defaultdict

DIR = Path(os.path.dirname(os.path.abspath(__file__)))

file_basename = Path(sys.argv[0]).stem
infile = DIR / "input.txt"
outfile = DIR / f"{file_basename}.txt"

sys.stdin = open(infile, "r")
sys.stdout = open(outfile, "w")


def add(p1, p2):
    return p1[0] + p2[0], p1[1] + p2[1]


def sub(p1, p2):
    return p1[0] - p2[0], p1[1] - p2[1]


grid = list(map(lambda s: list(s.rstrip("\n")), sys.stdin.readlines()))
positions = defaultdict(list)

for i, row in enumerate(grid):
    for j, x in enumerate(row):
        if x != ".":
            positions[x].append((i, j))

antinodes = set()
for _, locs in positions.items():
    for i in range(len(locs)):
        for j in range(i + 1, len(locs)):
            point1 = locs[i]
            point2 = locs[j]
            delta = sub(point2, point1)

            back = point1
            while 0 <= back[0] < len(grid) and 0 <= back[1] < len(grid[0]):
                antinodes.add(back)
                back = sub(back, delta)

            forward = point2
            while 0 <= forward[0] < len(grid) and 0 <= forward[1] < len(grid[0]):
                antinodes.add(forward)
                forward = add(forward, delta)


ttl = 0
for a, b in antinodes:
    if 0 <= a < len(grid) and 0 <= b < len(grid[0]):
        grid[a][b] = "#"
        ttl += 1
print(ttl)
