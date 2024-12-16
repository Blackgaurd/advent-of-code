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

    d4 = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    q = deque([(sx, sy, 0, 1)])
    inq = {(sx, sy, 0, 1)}
    dis = [[defaultdict(lambda: int(1e9)) for i in range(m)] for j in range(n)]
    dis[sx][sy][0, 1] = 0

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

    # print(dict(dis[7][3]))
    # print(dict(dis[8][3]))
    # print(dict(dis[7][2]))

    marked = set()
    q2 = deque([(ex, ey, -1, 0)])
    inq = {(ex, ey, -1, 0)}
    while q2:
        cx, cy, pdx, pdy = q2.popleft()
        marked.add((cx, cy))
        if (cx, cy) == (sx, sy):
            continue

        mindis = int(1e9)
        next_vis = []
        for (inc_dx, inc_dy), d_dis in dis[cx][cy].items():
            nx, ny = cx - inc_dx, cy - inc_dy

            adj_dis = d_dis
            if (inc_dx, inc_dy) != (pdx, pdy):
                adj_dis += 1000

            if adj_dis < mindis:
                mindis = adj_dis
                next_vis.clear()

            # not too sure why this logic works lol
            if (
                adj_dis == mindis
                and (nx, ny, inc_dx, inc_dy) not in inq
                and grid[nx][ny] != "#"
                and dis[nx][ny][inc_dx, inc_dy] < dis[cx][cy][inc_dx, inc_dy]
            ):
                next_vis.append((nx, ny, inc_dx, inc_dy))

        for x in next_vis:
            inq.add(x)
        q2.extend(next_vis)

    return marked


sx, sy = find_char(grid, "S")
ex, ey = find_char(grid, "E")
visited = bfs(grid, sx, sy, ex, ey)
print(len(visited))
