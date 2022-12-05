f = open("day5/input.txt", "r")

stacks = [[] for i in range(10)]
while "[" in (line := f.readline().rstrip("\n")):
    for s, i in enumerate(range(1, len(line), 4), start=1):
        if line[i] == " ":
            continue
        stacks[s].append(line[i])

for i in range(len(stacks)):
    stacks[i].reverse()


f.readline()
for line in map(lambda x: x.rstrip("\n"), f.readlines()):
    tokens = line.split()
    n, a, b = map(int, [tokens[1], tokens[3], tokens[5]])
    for i in range(n):
        stacks[b].append(stacks[a].pop())

for stack in stacks:
    if stack:
        print(end=stack[-1])

print()

f.close()