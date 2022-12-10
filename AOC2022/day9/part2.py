f = open("day9/input.txt")

d4 = {
    "U": (0, 1),
    "D": (0, -1),
    "R": (1, 0),
    "L": (-1, 0),
}

visited = set()
visited.add((0, 0))
knots = [[0, 0] for i in range(10)]

for d, x in map(lambda x: x.rstrip("\n").split(), f):
    # brute force bc lazy
    dx, dy = d4[d]
    for i in range(int(x)):
        knots[0][0] += dx
        knots[0][1] += dy

        for i in range(1, 10):
            diff_x = knots[i - 1][0] - knots[i][0]
            diff_y = knots[i - 1][1] - knots[i][1]
            if abs(diff_x) == 2 and abs(diff_y) == 2:
                sx = 1 if diff_x == 2 else -1
                sy = 1 if diff_y == 2 else -1
                knots[i][0] += sx
                knots[i][1] += sy
            elif abs(diff_x) == 2:
                knots[i][0] += 1 if diff_x == 2 else -1
                knots[i][1] = knots[i - 1][1]
            elif abs(diff_y) == 2:
                knots[i][1] += 1 if diff_y == 2 else -1
                knots[i][0] = knots[i - 1][0]

        visited.add(tuple(knots[-1]))

print(len(visited))

f.close()
