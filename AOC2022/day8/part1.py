from itertools import product
from pprint import pprint

f = open("day8/input.txt")

arr = []
for line in map(lambda x: x.rstrip("\n"), f):
    new = list(line)
    new.insert(0, "0")
    new.append("0")
    arr.append(new)

arr.insert(0, ["0" for i in range(len(arr[0]))])
arr.append(["0" for i in range(len(arr[0]))])

n, m = len(arr), len(arr[0])
seen = [[False for i in range(n)] for j in range(m)]

for i in range(1, n - 1):
    row_max = '/' # lower ascii value than 0
    for j in range(1, m - 1):
        if arr[i][j] > row_max:
            row_max = arr[i][j]
            seen[i][j] = True
    row_max = '/'
    for j in range(m - 2, 0, -1):
        if arr[i][j] > row_max:
            row_max = arr[i][j]
            seen[i][j] = True

for j in range(m):
    col_max = '/'
    for i in range(1, n - 1):
        if arr[i][j] > col_max:
            col_max = arr[i][j]
            seen[i][j] = True
    col_max = '/'
    for i in range(n - 2, 0, -1):
        if arr[i][j] > col_max:
            col_max = arr[i][j]
            seen[i][j] = True

ttl = 0
for i in range(1, n - 1):
    for j in range(1, m - 1):
        ttl += seen[i][j]

print(ttl)

f.close()
