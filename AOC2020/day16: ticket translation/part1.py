import sys
import os

DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(f"{DIR}/input.txt", "r")
sys.stdout = open(f"{DIR}/part1.txt", "w")

ranges = []
stdin = iter(sys.stdin.read().splitlines() + [""])
while cur := next(stdin):
    _, unparsed = cur.split(": ")
    (a, b), (c, d) = map(lambda x: x.split("-"), unparsed.split(" or "))
    ranges.extend([range(int(a), int(b) + 1), range(int(c), int(d) + 1)])

for i in range(4):
    next(stdin)

ttl = 0
while cur := next(stdin):
    for num in map(int, cur.split(",")):
        if all(num not in r for r in ranges):
            ttl += num

print(ttl)
