f = open("day14/input.txt", "r")

paths = []
min_x, min_y = 1000, 1000
max_x, max_y = 0, 0
for line in map(lambda x: x.rstrip("\n"), f):
    args = line.split(" -> ")
    cur = []
    for x, y in map(lambda x: map(int, x.split(",")), args):
        min_x = min(min_x, x)
        min_y = min(min_y, y)
        max_x = max(max_x, x)
        max_y = max(max_y, y)
        cur.append([y, x])
    paths.append(cur)

paths = list(map(lambda x: list(map(lambda y: [y[0], y[1] - min_x], x)), paths))
cave = [[0 for _ in range(max_x - min_x + 1)] for _ in range(max_y + 1)]

for p in paths:
    for i in range(1, len(p)):
        cur, prev = p[i], p[i - 1]
        if cur[0] == prev[0]:
            for x in range(min(cur[1], prev[1]), max(cur[1], prev[1]) + 1):
                cave[cur[0]][x] = 1
        else:
            for y in range(min(cur[0], prev[0]), max(cur[0], prev[0]) + 1):
                cave[y][cur[1]] = 1


def print_cave():
    global cave
    for row in cave:
        print("".join(map(lambda x: "#" if x == 1 else ".", row)))


def add_sand():
    global cave, min_x
    x = 500 - min_x
    y = 0
    while True:
        if y + 1 == len(cave) or x - 1 < 0 or x + 1 >= len(cave[0]):
            return False
        if cave[y + 1][x] == 0:
            y += 1
        elif cave[y + 1][x - 1] == 0:
            y += 1
            x -= 1
        elif cave[y + 1][x + 1] == 0:
            y += 1
            x += 1
        else:
            cave[y][x] = 1
            return True

cnt = 0
while add_sand():
    cnt += 1

f.close()
