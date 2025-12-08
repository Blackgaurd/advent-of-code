import sys
import os
from pathlib import Path

DIR = Path(os.path.dirname(os.path.abspath(__file__)))

file_basename = Path(sys.argv[0]).stem
infile = DIR / "input.txt"

sys.stdin = open(infile, "r")

points = []
parents = dict()
for line in map(lambda ln: ln.strip("\n"), sys.stdin.readlines()):
    x, y, z = map(int, line.split(","))
    points.append((x, y, z))
    parents[(x, y, z)] = (x, y, z)


def distance(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2


def find_parent(p):
    global parents
    while parents[p] != p:
        p = parents[p]
    return p


def union(p1, p2):
    global parents
    parent1 = find_parent(p1)
    parent2 = find_parent(p2)
    if parent1 != parent2:
        parents[parent1] = parent2


dis = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dis.append((distance(points[i], points[j]), i, j))
dis.sort(key=lambda t: t[0])

circuits = 1000
for i in range(len(dis)):
    _, pi, pj = dis[i]
    parent_i = find_parent(points[pi])
    parent_j = find_parent(points[pj])
    union(points[pi], points[pj])

    if parent_i != parent_j:
        circuits -= 1
    if circuits == 1:
        print(points[pi][0] * points[pj][0])
        break
