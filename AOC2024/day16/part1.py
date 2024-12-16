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
for line in sys.stdin:
    grid.append(list(line.strip("\n")))


def find_char(grid, char):
    n = len(grid)
    m = len(grid[0])
    for i in range(n):
        for j in range(m):
            if grid[i][j] == char:
                return i, j
    return n, m


def bfs(grid, sx, sy, ex, ey):
    n = len(grid)
    m = len(grid[0])

    q = deque([(sx, sy, 0, 1)])
    inq = {(sx, sy, 0, 1)}
    dis = [[defaultdict(lambda: int(1e9)) for i in range(m)] for j in range(n)]
    dis[sx][sy][0, 1] = 0

    d4 = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    while q:
        cx, cy, cdx, cdy = q.popleft()
        inq.remove((cx, cy, cdx, cdy))

        for d in d4:
            if d == (cdx, cdy):
                continue
            elif d == (-cdx, -cdy):
                dis[cx][cy][d] = min(dis[cx][cy][d], dis[cx][cy][cdx, cdy] + 2000)
            else:
                dis[cx][cy][d] = min(dis[cx][cy][d], dis[cx][cy][cdx, cdy] + 1000)

        for dx, dy in d4:
            nx, ny = cx + dx, cy + dy
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            if grid[nx][ny] == "#":
                continue

            if dis[nx][ny][dx, dy] > dis[cx][cy][dx, dy] + 1:
                dis[nx][ny][dx, dy] = dis[cx][cy][dx, dy] + 1
                if (nx, ny, dx, dy) not in inq:
                    inq.add((nx, ny, dx, dy))
                    q.append((nx, ny, dx, dy))

    return dis[ex][ey]


sx, sy = find_char(grid, "S")
ex, ey = find_char(grid, "E")
print(min(bfs(grid, sx, sy, ex, ey).values()))
