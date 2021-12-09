import sys
import os

DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(DIR + "/input.txt", "r")
sys.stdout = open(DIR + "/part1.txt", "w")

instructions = [(line[0], int(line[1:])) for line in sys.stdin]
# E N W S
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
x, y, d = 0, 0, 0
for direction, val in instructions:
    if direction == 'L':
        val //= 90
        d += val
        d %= 4
    elif direction == 'R':
        val //= 90
        d -= val
        if d < 0:
            d += 4
    elif direction == 'E':
        x += dx[0] * val
        y += dy[0] * val
    elif direction == 'N':
        x += dx[1] * val
        y += dy[1] * val
    elif direction == 'W':
        x += dx[2] * val
        y += dy[2] * val
    elif direction == 'S':
        x += dx[3] * val
        y += dy[3] * val
    else:
        x += dx[d] * val
        y += dy[d] * val

print(abs(x) + abs(y))
