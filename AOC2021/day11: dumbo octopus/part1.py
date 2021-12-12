import sys
import os

DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(f"{DIR}/input.txt", "r")
sys.stdout = open(f"{DIR}/part1.txt", "w")

arr = [list(map(int, list(line))) for line in sys.stdin.read().splitlines()]
n, m = len(arr), len(arr[0])
dx = [1, 0, -1, 0, 1, 1, -1, -1]
dy = [0, 1, 0, -1, 1, -1, 1, -1]

total_flashes = 0

def count():
    for i in range(n):
        for j in range(m):
            if arr[i][j] > 9:
                return True
    return False

def flash():
    for i in range(n):
        for j in range(m):
            if arr[i][j] > 9:
                arr[i][j] = -1
                for k in range(8):
                    x, y = i + dx[k], j + dy[k]
                    if 0 <= x < n and 0 <= y < m and arr[x][y] != -1:
                        arr[x][y] += 1

STEPS = 100
for _ in range(STEPS):
    # increment everything by 1
    for i in range(n):
        for j in range(m):
            arr[i][j] += 1

    # flash ones with 9 or greater
    while count():
        flash()
        flash()

    # set all flashed ones to 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == -1:
                total_flashes += 1
                arr[i][j] = 0

print(total_flashes)
