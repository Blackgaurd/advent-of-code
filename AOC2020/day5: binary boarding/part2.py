import sys
import os

DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(DIR + "/input.txt", "r")
sys.stdout = open(DIR + "/part2.txt", "w")


def parse(code):
    lo, hi = 0, 127
    for char in code[:7]:
        if char == "B":
            lo = (lo + hi) // 2 + 1
        else:
            hi = (lo + hi) // 2
    x = lo
    lo, hi = 0, 7
    for char in code[7:]:
        if char == "R":
            lo = (lo + hi) // 2 + 1
        else:
            hi = (lo + hi) // 2
    return x, lo

seats = [[False for _ in range(8)] for _ in range(128)]
for line in sys.stdin:
    x, y = parse(line)
    seats[x][y] = True

for i in range(128):
    for j in range(8):
        if not seats[i][j] and seats[i][j-1] and seats[i][j+1]:
            print(i * 8 + j)
