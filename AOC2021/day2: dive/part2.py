import sys
import os

DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(f"{DIR}/input.txt", "r")
sys.stdout = open(f"{DIR}/part2.txt", "w")

x, y, aim = 0, 0, 0
for line in sys.stdin:
    direction, cnt = line.split()
    cnt = int(cnt)
    if direction[0] == 'f':
        x += cnt
        y += cnt * aim
    elif direction[0] == 'u':
        aim -= cnt
    else:
        aim += cnt

print(x * y)
