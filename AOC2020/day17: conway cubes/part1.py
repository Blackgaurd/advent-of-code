import os
import sys

DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(f"{DIR}/input.txt", "r")
sys.stdout = open(f"{DIR}/part1.txt", "w")

arr = sys.stdin.read().splitlines()
alive = set()
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j] == "#":
            alive.add((i, j, 0))

dx = [-1, -1, -1, 0, 0, 0, 1, 1, 1, -1, -1, -1, 0, 0, 1, 1, 1, -1, -1, -1, 0, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1, -1, 0, 1]
dz = [ -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]


def get_cnt(pos):
    return sum(
        (pos[0] + dx[i], pos[1] + dy[i], pos[2] + dz[i]) in alive
        for i in range(26)
    )

def cycle(alive):
    tmp = alive.copy()
    minx, maxx = min(x[0] - 1 for x in alive), max(x[0] + 1 for x in alive)
    miny, maxy = min(x[1] - 1 for x in alive), max(x[1] + 1 for x in alive)
    minz, maxz = min(x[2] - 1 for x in alive), max(x[2] + 1 for x in alive)
    for x in range(minx, maxx + 1):
        for y in range(miny, maxy + 1):
            for z in range(minz, maxz + 1):
                cnt = get_cnt((x, y, z))
                if (x, y, z) in alive and cnt not in [2, 3]:
                    tmp.remove((x, y, z))
                elif cnt == 3:
                    tmp.add((x, y, z))
    return tmp

for i in range(6):
    alive = cycle(alive)

print(len(alive))
