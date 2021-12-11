import sys
import os
from collections import deque

DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(f"{DIR}/input.txt", "r")
sys.stdout = open(f"{DIR}/part1.txt", "w")

arr = list(map(int, input().split(",")))
out = []
mem = {}


def add(val, i):
    if val not in mem:
        mem[val] = deque(maxlen=2)
    mem[val].append(i)


for i in range(2020):
    if i < len(arr):
        out.append(arr[i])
        add(arr[i], i)
        continue
    prev = out[-1]
    if len(mem[prev]) == 1:
        out.append(0)
        add(0, i)
    else:
        nxt = i - mem[prev][0] - 1
        out.append(nxt)
        add(nxt, i)

print(out[-1])