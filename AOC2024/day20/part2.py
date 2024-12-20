import sys
import os
from pathlib import Path
from collections import deque, defaultdict

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


def euc_dis(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def bfs(grid, start):
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

    return dis


def is_valid_cheat(grid, start, end):
    ed = euc_dis(start, end)
    if ed <= 1 or ed > 20:
        return False

    for i in range(min(start[0], end[0]), max(start[0], end[0]) + 1):
        for j in range(min(start[1], end[1]), max(start[1], end[1]) + 1):
            if grid[i][j] == "#":
                return True
    return False


start = find_char(grid, "S")
end = find_char(grid, "E")

start_dis = bfs(grid, start)
end_dis = bfs(grid, end)

empties = []
for i, row in enumerate(grid):
    for j, x in enumerate(row):
        if x != "#":
            empties.append((i, j))

ans = 0
for cheat_start in empties:
    for cheat_end in empties:
        if not is_valid_cheat(grid, cheat_start, cheat_end):
            continue

        ttl_dis = (
            start_dis[cheat_start[0]][cheat_start[1]]
            + end_dis[cheat_end[0]][cheat_end[1]]
            + euc_dis(cheat_start, cheat_end)
        )
        saved = start_dis[end[0]][end[1]] - ttl_dis
        if saved >= 100:
            ans += 1

print(ans)
