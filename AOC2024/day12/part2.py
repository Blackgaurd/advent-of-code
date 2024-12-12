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


def add_tup(a, b):
    return (a[0] + b[0], a[1] + b[1])


def turn_ccw(d):
    if d == (0, 1):
        return (-1, 0)
    if d == (-1, 0):
        return (0, -1)
    if d == (0, -1):
        return (1, 0)
    if d == (1, 0):
        return (0, 1)


def turn_cw(d):
    for _ in range(3):
        d = turn_ccw(d)
    return d


def sides(positions_set: set[tuple[int, int]], plant: str):
    global grid

    positions_covered = set()

    def trav(pos):
        nonlocal positions_covered

        d = (0, 1)
        start_d = d
        start_pos = pos
        ans = 0

        while True:
            if ans != 0:
                if d == start_d and pos == start_pos:
                    break
            positions_covered.add(pos)
            in_front = add_tup(pos, d)
            if in_front in positions_set:
                # turn CCW
                ans += 1
                d = turn_ccw(d)
                continue

            under_front = add_tup(in_front, turn_cw(d))
            if under_front not in positions_set:
                pos = under_front
                ans += 1
                d = turn_cw(d)
                continue

            pos = add_tup(pos, d)

        return ans

    n = len(grid)
    m = len(grid[0])
    ans = 0
    for i, j in positions_set:
        pos = (i - 1, j)
        if (
            grid[i][j] == plant
            and (i - 1 < 0 or grid[i - 1][j] != plant)
            and pos not in positions_covered
        ):
            # t = trav(pos)
            ans += trav(pos)
    return ans


def bfs(grid, sx, sy, vis: set[tuple[int, int]]):
    if (sx, sy) in vis:
        return 0, 0

    n = len(grid)
    m = len(grid[0])

    d4 = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    q = deque([(sx, sy)])
    cur_vis = set()
    vis.add((sx, sy))
    cur_vis.add((sx, sy))
    plant = grid[sx][sy]
    area = 0

    while q:
        cx, cy = q.popleft()
        area += 1

        for dx, dy in d4:
            nx, ny = cx + dx, cy + dy
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            if grid[nx][ny] != plant:
                continue
            if (nx, ny) not in vis:
                vis.add((nx, ny))
                cur_vis.add((nx, ny))
                q.append((nx, ny))

    return sides(cur_vis, plant), area


ans = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        s, a = bfs(grid, i, j, vis)
        ans += s * a
print(ans)
