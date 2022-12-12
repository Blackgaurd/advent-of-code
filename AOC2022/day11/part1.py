f = open("day11/input.txt")

lines = f.readlines()
parse_iter = zip(*[map(lambda x: x.rstrip("\n").strip(), lines)] * 7)

monkeys = []
for group in parse_iter:
    items = list(map(int, group[1].split(":")[-1].split(",")))
    func = group[2].split("=")[-1].strip()
    condition = int(group[3].split()[-1])
    true = int(group[4].split()[-1])
    false = int(group[5].split()[-1])
    monkeys.append({
        "items": items,
        "func": func,
        "condition": condition,
        "true": true,
        "false": false,
    })

total_items = [0 for i in range(len(monkeys))]

for r in range(1, 20 + 1):
    for i, monkey in enumerate(monkeys):
        total_items[i] += len(monkey["items"])
        for item in monkey["items"]:
            item = eval(monkey["func"], {"old": item})
            item //= 3
            if item % monkey["condition"] == 0:
                monkeys[monkey["true"]]["items"].append(item)
            else:
                monkeys[monkey["false"]]["items"].append(item)
        monkey["items"].clear()

total_items.sort()
print(total_items[-1] * total_items[-2])


f.close()
