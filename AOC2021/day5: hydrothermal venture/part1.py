import sys
import os

DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(f"{DIR}/input.txt", "r")
sys.stdout = open(f"{DIR}/part1.txt", "w")


class line:
    def __init__(self, unparsed):
        (x1, y1), (x2, y2) = map(lambda x: x.split(",")[::-1], unparsed.split("->"))
        self.x1 = int(x1)
        self.y1 = int(y1)
        self.x2 = int(x2)
        self.y2 = int(y2)

    def __repr__(self) -> str:
        return f"({self.x1},{self.y1}), ({self.x2},{self.y2})"


lines = []
for coords in sys.stdin:
    cur = line(coords)
    if cur.x1 == cur.x2 or cur.y1 == cur.y2:
        lines.append(cur)

# brute force because I'm lazy
arr = [[0 for _ in range(1000)] for _ in range(1000)]
for cur in lines:
    if cur.x1 == cur.x2:
        for y in range(min(cur.y1, cur.y2), max(cur.y1, cur.y2) + 1):
            arr[cur.x1][y] += 1
    elif cur.y1 == cur.y2:
        for x in range(min(cur.x1, cur.x2), max(cur.x1, cur.x2) + 1):
            arr[x][cur.y1] += 1

ans = sum(sum(i >= 2 for i in j) for j in arr)
print(ans)
