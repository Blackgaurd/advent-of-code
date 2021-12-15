import os
import sys

DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(f"{DIR}/test.txt", "r")
sys.stdout = open(f"{DIR}/part2.txt", "w")

arr = sys.stdin.read().splitlines()
alive = set()
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j] == "#":
            alive.add((i, j, 0, 0))

dirs = [-1, 0, 1]

def precompute_cnts():
    ret = {}
    for coord in alive:
        for dx in dirs:
            for dy in dirs:
                for dz in dirs:
                    for dw in dirs:
                        if dx == 0 and dy == 0 and dz == 0 and dw == 0:
                            continue
                        new = (coord[0] + dx, coord[1] + dy, coord[2] + dz, coord[3] + dw)
                        if new not in ret:
                            ret[new] = 0
                        ret[new] += 1
    return ret

def cycle(alive):
    tmp = alive.copy()
    precomputed = precompute_cnts()
    get_cnt = lambda x: precomputed.get(x, 0)
    minx, maxx = min(x[0] - 1 for x in alive), max(x[0] + 1 for x in alive)
    miny, maxy = min(x[1] - 1 for x in alive), max(x[1] + 1 for x in alive)
    minz, maxz = min(x[2] - 1 for x in alive), max(x[2] + 1 for x in alive)
    minw, maxw = min(x[3] - 1 for x in alive), max(x[3] + 1 for x in alive)
    for x in range(minx, maxx + 1):
        for y in range(miny, maxy + 1):
            for z in range(minz, maxz + 1):
                for w in range(minw, maxw + 1):
                    cnt = get_cnt((x, y, z, w))
                    if (x, y, z, w) in alive and cnt not in [2, 3]:
                        tmp.remove((x, y, z, w))
                    elif cnt == 3:
                        tmp.add((x, y, z, w))
    return tmp

for i in range(6):
    alive = cycle(alive)

print(len(alive))
