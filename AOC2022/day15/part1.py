import re

f = open("day15/input.txt", "r")

pattern = r"x=(-?\d+), y=(-?\d+)"
sensors = []
for line in f:
    coords = re.findall(pattern, line)
    coords[0] = tuple(map(int, coords[0]))
    coords[1] = tuple(map(int, coords[1]))
    sensors.append(coords)


def dis(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


y = 2_000_000
covered_ranges = []
for s, b in sensors:
    max_dis = dis(s, b)
    y_dis = abs(s[1] - y)
    if y_dis > max_dis:
        continue

    x_dis = max_dis - y_dis
    covered_ranges.append((s[0] - x_dis, s[0] + x_dis))

final_ranges = []
for begin, end in sorted(covered_ranges):
    if final_ranges and final_ranges[-1][1] >= begin - 1:
        final_ranges[-1][1] = max(final_ranges[-1][1], end)
    else:
        final_ranges.append([begin, end])

ttl = 0
for begin, end in final_ranges:
    ttl += end - begin + 1

beacons = set()
for _, b in sensors:
    beacons.add(b)

for b in beacons:
    if b[1] == y:
        ttl -= 1

print(ttl)

f.close()
