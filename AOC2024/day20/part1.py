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
for line in map(lambda s: s.strip("\n"), sys.stdin):
    grid.append(list(line))


def find_char(grid, char):
    for i, row in enumerate(grid):
        for j, x in enumerate(row):
            if x == char:
                return i, j
    return -1, -1


def bfs(grid, start, end):
    n = len(grid)
    m = len(grid[0])

    d4 = ((-1, 0), (1, 0), (0, 1), (0, -1))

    sx, sy = start
    dis = [[int(1e9) for _ in range(m)] for _ in range(n)]
    dis[sx][sy] = 0

    q = deque([start])
    while q:
        cx, cy = q.pop()
        for dx, dy in d4:
            nx, ny = cx + dx, cy + dy
            if grid[nx][ny] == "#":
                continue

            if dis[nx][ny] > dis[cx][cy] + 1:
                dis[nx][ny] = dis[cx][cy] + 1
                q.append((nx, ny))

    ex, ey = end
    return dis[ex][ey]


start = find_char(grid, "S")
end = find_char(grid, "E")

ans = 0
no_cheat = bfs(grid, start, end)
for i in range(1, len(grid) - 1):
    for j in range(1, len(grid[0]) - 1):
        if grid[i][j] != "#":
            continue
        grid[i][j] = "."

        dis = bfs(grid, start, end)
        saved = no_cheat - dis
        if saved >= 100:
            ans += 1

        grid[i][j] = "#"

print(ans)
