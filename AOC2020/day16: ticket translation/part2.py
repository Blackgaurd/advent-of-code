import sys
import os

DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(f"{DIR}/input.txt", "r")
sys.stdout = open(f"{DIR}/part2.txt", "w")

ranges = {}
range_list = []
stdin = iter(sys.stdin.read().splitlines() + [""])
while cur := next(stdin):
    name, unparsed = cur.split(": ")
    (a, b), (c, d) = map(lambda x: x.split("-"), unparsed.split(" or "))
    a, b, c, d = map(int, [a, b, c, d])
    ranges[name] = range(a, b + 1), range(c, d + 1)
    range_list.extend([range(a, b + 1), range(c, d + 1)])

next(stdin)

your_ticket = list(map(int, next(stdin).split(",")))

next(stdin)
next(stdin)

tickets = []
while cur := next(stdin):
    cur_tickets = list(map(int, cur.split(",")))
    for num in cur_tickets:
        if all(num not in r for r in range_list):
            break
    else:
        tickets.append(cur_tickets)


def within(val, cur_ranges):
    return any(val in r for r in cur_ranges)


possible = [set() for _ in range(len(tickets[0]))]
for i in range(len(tickets[0])):
    for key, val in ranges.items():
        if all(within(tickets[i], val) for tickets in tickets):
            possible[i].add(key)

final_values = ["" for i in range(len(tickets[0]))]
while sum(i > 0 for i in map(len, possible)):
    for i in range(len(possible)):
        if len(possible[i]) == 1:
            (final_values[i],) = possible[i]
            for item in possible:
                item.discard(final_values[i])

ans = 1
for i in range(len(final_values)):
    if final_values[i].startswith("departure"):
        ans *= your_ticket[i]

print(ans)
