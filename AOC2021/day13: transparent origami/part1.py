import sys
import os

DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(f"{DIR}/input.txt", "r")
sys.stdout = open(f"{DIR}/part1.txt", "w")

stdin = iter(sys.stdin.read().splitlines() + [""])
coords = set()

def fold_y(line):
    newset = set()
    for coord in coords.copy():
        if coord[1] > line:
            newset.add((coord[0], line - (coord[1] - line)))
            coords.remove(coord)
    coords.update(newset)

def fold_x(line):
    newset = set()
    for coord in coords.copy():
        if coord[0] < line:
            newset.add((line + line - coord[0], coord[1]))
            coords.remove(coord)
    coords.update(newset)

while cur := next(stdin):
    coords.add(tuple(map(int, cur.split(","))))

cur = next(stdin)
_, _, instruction = cur.split()
axis, line = instruction.split("=")
if axis == "x":
    fold_x(int(line))
else:
    fold_y(int(line))

print(len(coords))