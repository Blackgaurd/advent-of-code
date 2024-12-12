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

grid = [line.rstrip("\n") for line in sys.stdin.readlines()]
vis = set()


def bfs(grid, sx, sy, vis: set[tuple[int, int]]):
    if (sx, sy) in vis:
        return 0, 0

    n = len(grid)
    m = len(grid[0])

    d4 = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    q = deque([(sx, sy)])
    vis.add((sx, sy))
    plant = grid[sx][sy]
    perimeter = 0
    area = 0

    while q:
        cx, cy = q.popleft()
        area += 1

        for dx, dy in d4:
            nx, ny = cx + dx, cy + dy
            if not (0 <= nx < n and 0 <= ny < m):
                perimeter += 1
                continue
            if grid[nx][ny] != plant:
                perimeter += 1
                continue
            if (nx, ny) not in vis:
                vis.add((nx, ny))
                q.append((nx, ny))

    return perimeter, area


ans = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        p, a = bfs(grid, i, j, vis)
        ans += p * a
print(ans)
