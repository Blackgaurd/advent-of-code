from itertools import product
from pprint import pprint

f = open("day8/input.txt")

arr = []
for line in map(lambda x: x.rstrip("\n"), f):
    new = list(line)
    new.insert(0, "/")
    new.append("/")
    arr.append(new)

arr.insert(0, ["/" for i in range(len(arr[0]))])
arr.append(["/" for i in range(len(arr[0]))])

n, m = len(arr), len(arr[0])
d4 = [(0, 1), (0, -1), (1, 0), (-1, 0)]
ans = 0
for i, j in product(range(2, n - 2), range(2, m - 2)):
    prod = 1
    for di, dj in d4:
        new_arr = []
        x, y = i + di, j + dj
        while arr[x][y] != "/":
            new_arr.append(arr[x][y])
            x += di
            y += dj

        arr_max = "/"
        cnt = 0
        for k in new_arr:
            cnt += 1
            if k >= arr[i][j]:
                break
        prod *= cnt
    ans = max(ans, prod)

print(ans)

f.close()
