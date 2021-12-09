import sys
import os

DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(DIR + "/input.txt", "r")
sys.stdout = open(DIR + "/part2.txt", "w")


def rotate(px, py):
    return py, -px


instructions = [(line[0], int(line[1:])) for line in sys.stdin]
# E N W S
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
bx, by = 0, 0
wx, wy = 10, -1
for direction, val in instructions:
    if direction == "E":
        wx += dx[0] * val
        wy += dy[0] * val
    elif direction == "N":
        wx += dx[1] * val
        wy += dy[1] * val
    elif direction == "W":
        wx += dx[2] * val
        wy += dy[2] * val
    elif direction == "S":
        wx += dx[3] * val
        wy += dy[3] * val
    elif direction == "F":
        bx += wx * val
        by += wy * val
    elif direction == "L":
        for i in range(val // 90):
            wx, wy = rotate(wx, wy)
    elif direction == "R":
        for i in range(4 - val // 90):
            wx, wy = rotate(wx, wy)

print(abs(bx) + abs(by))
