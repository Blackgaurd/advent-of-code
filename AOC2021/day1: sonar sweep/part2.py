import sys
import os
from collections import deque

DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(f"{DIR}/input.txt", "r")
sys.stdout = open(f"{DIR}/part2.txt", "w")

cnt = 0

a = deque(maxlen=3)
for i in range(3):
    a.append(int(sys.stdin.readline()))

for num in sys.stdin:
    sum1 = sum(a)
    a.append(int(num))
    if sum(a) > sum1:
        cnt += 1

print(cnt)
