import sys
import os
from pathlib import Path
from enum import IntEnum, auto
from collections import deque

DIR = Path(os.path.dirname(os.path.abspath(__file__)))
infile = DIR / "input.txt"
sys.stdin = open(infile, "r")


class GridState(IntEnum):
    INSIDE = auto()
    BORDER = auto()
    OUTSIDE = auto()


coords = []
x_s = set()
y_s = set()
for line in map(lambda ln: ln.strip("\n"), sys.stdin.readlines()):
    x, y = map(int, line.split(","))
    coords.append((x, y))
    x_s.add(x)
    y_s.add(y)

x_s = sorted(x_s)
y_s = sorted(y_s)


def build_map(sorted_points):
    mp = dict()
    idx = 1
    for i, p in enumerate(sorted_points):
        if i != 0 and sorted_points[i - 1] + 1 != p:
            idx += 1
        mp[p] = idx
        idx += 1
    return mp


def map_point(point, x_map, y_map):
    x, y = point
    return x_map[x], y_map[y]


def print_grid(grid, fill1=None, fill2=None):
    fill = False
    if fill1 is not None and fill2 is not None:
        fill = True
        min_x = min(fill1[0], fill2[0])
        max_x = max(fill1[0], fill2[0])
        min_y = min(fill1[1], fill2[1])
        max_y = max(fill1[1], fill2[1])
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if fill and min_x <= i <= max_x and min_y <= j <= max_y:
                print(end="@")
                continue
            if cell == GridState.OUTSIDE:
                print(end="o")
            elif cell == GridState.INSIDE:
                print(end="I")
            else:
                print(end="B")
        print()


x_map = build_map(x_s)
y_map = build_map(y_s)
grid = [
    [GridState.INSIDE for y in range(max(y_map.values()) + 1)]
    for x in range(max(x_map.values()) + 1)
]
for i in range(len(coords)):
    cur = map_point(coords[i], x_map, y_map)
    prev = map_point(coords[i - 1], x_map, y_map)

    min_x = min(cur[0], prev[0])
    max_x = max(cur[0], prev[0])
    min_y = min(cur[1], prev[1])
    max_y = max(cur[1], prev[1])
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            grid[x][y] = GridState.BORDER


# flood fill
q = deque()
for x, y in (
    (0, 0),
    (0, len(grid[0]) - 1),
    (len(grid) - 1, 0),
    (len(grid) - 1, len(grid[0]) - 1),
):
    if grid[x][y] == GridState.INSIDE:
        grid[x][y] = GridState.OUTSIDE
        q.append((x, y))
d4 = ((0, 1), (0, -1), (1, 0), (-1, 0))
while q:
    cx, cy = q.popleft()
    for dx, dy in d4:
        nx = cx + dx
        ny = cy + dy
        if nx < 0 or nx >= len(grid):
            continue
        if ny < 0 or ny >= len(grid[0]):
            continue
        if grid[nx][ny] != GridState.INSIDE:
            continue
        grid[nx][ny] = GridState.OUTSIDE
        q.append((nx, ny))


def is_valid(point1, point2, x_map, y_map, grid):
    x1, y1 = map_point(point1, x_map, y_map)
    x2, y2 = map_point(point2, x_map, y_map)

    min_x = min(x1, x2)
    max_x = max(x1, x2)
    min_y = min(y1, y2)
    max_y = max(y1, y2)
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            if grid[x][y] == GridState.OUTSIDE:
                return False
    return True


def calc_area(a, b):
    length = abs(a[0] - b[0]) + 1
    width = abs(a[1] - b[1]) + 1
    return length * width


max_area = 0
best_1 = None
best_2 = None
for i in range(len(coords)):
    for j in range(i + 1, len(coords)):
        point1 = coords[i]
        point2 = coords[j]
        if is_valid(point1, point2, x_map, y_map, grid):
            area = calc_area(point1, point2)
            if area > max_area:
                max_area = max(max_area, area)
                best_1 = point1
                best_2 = point2
print(max_area)
