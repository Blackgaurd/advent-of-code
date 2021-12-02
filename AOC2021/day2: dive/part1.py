import sys
import os

DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(f"{DIR}/input.txt", "r")
sys.stdout = open(f"{DIR}/part1.txt", "w")

x, y = 0, 0
for line in sys.stdin:
    direction, cnt = line.split()
    cnt = int(cnt)
    if direction[0] == 'f':
        x += cnt
    elif direction[0] == 'd':
        y += cnt
    else:
        y -= cnt

print(x * y)
