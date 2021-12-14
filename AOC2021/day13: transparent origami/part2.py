import sys
import os
from pprint import pprint

DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(f"{DIR}/input.txt", "r")
sys.stdout = open(f"{DIR}/part2.txt", "w")

stdin = iter(sys.stdin.read().splitlines() + [""])
coords = set()


def fold_y(line):
    newset = set()
    for coord in coords.copy():
        if coord[0] > line:
            newset.add((line + line - coord[0], coord[1]))
            coords.remove(coord)
    coords.update(newset)


def fold_x(line):
    newset = set()
    for coord in coords.copy():
        if coord[1] > line:
            newset.add((coord[0], line + line - coord[1]))
            coords.remove(coord)
    coords.update(newset)


while cur := next(stdin):
    nums = tuple(map(int, cur.split(",")))
    nums = (nums[1], nums[0])
    coords.add(nums)

while cur := next(stdin):
    _, _, instruction = cur.split()
    axis, line = instruction.split("=")
    if axis == "x":
        fold_x(int(line))
    else:
        fold_y(int(line))

mx = max(map(lambda x: x[1], coords))
my = max(map(lambda x: x[0], coords))
arr = [["." for i in range(mx + 1)] for j in range(my + 1)]

for coord in coords:
    arr[coord[0]][coord[1]] = "#"

for line in arr:
    print("".join(line))
