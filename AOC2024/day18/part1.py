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

n = 70

d4 = [(-1, 0), (1, 0), (0, 1), (0, -1)]

dis = defaultdict(lambda: int(1e9))
dis[0, 0] = 0

take = 1024
for _ in range(take):
    a, b = map(int, input().split(","))
    dis[a, b] = -1

q = deque([(0, 0)])
while q:
    cx, cy = q.popleft()

    for dx, dy in d4:
        nx, ny = cx + dx, cy + dy
        if nx < 0 or nx > n:
            continue
        if ny < 0 or ny > n:
            continue

        if dis[nx, ny] > dis[cx, cy] + 1:
            dis[nx, ny] = dis[cx, cy] + 1
            q.append((nx, ny))

print(dis[n, n])
