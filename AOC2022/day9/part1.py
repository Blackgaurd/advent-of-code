f = open("day9/input.txt")

d4 = {
    "U": (0, 1),
    "D": (0, -1),
    "R": (1, 0),
    "L": (-1, 0),
}

visited = set()
visited.add((0, 0))
head = [0, 0]
tail = [0, 0]

for d, x in map(lambda x: x.rstrip("\n").split(), f):
    # brute force bc lazy
    dx, dy = d4[d]
    for i in range(int(x)):
        head[0] += dx
        head[1] += dy

        diff_x = head[0] - tail[0]
        diff_y = head[1] - tail[1]
        if diff_x == 2:
            tail[0] += 1
            tail[1] = head[1]
        elif diff_x == -2:
            tail[0] -= 1
            tail[1] = head[1]
        if diff_y == 2:
            tail[1] += 1
            tail[0] = head[0]
        elif diff_y == -2:
            tail[1] -= 1
            tail[0] = head[0]

        visited.add(tuple(tail))

print(len(visited))

f.close()
