import sys
import os

DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(DIR + "/input.txt", "r")
sys.stdout = open(DIR + "/part2.txt", "w")

instructions = []
for line in sys.stdin:
    a, b = line.split()
    b = int(b)
    instructions.append((a[0], b))


def check():
    i = 0
    x = 0
    completed = [False for _ in range(len(instructions))]
    while i < len(instructions):
        if completed[i]:
            return -1
        a, b = instructions[i]
        completed[i] = True
        if a == "j":
            i += b
        else:
            i += 1
            if a == "a":
                x += b
    return x


for i in range(len(instructions)):
    # swap
    a, b = instructions[i]
    if a == "j":
        instructions[i] = ("n", b)
    elif a == "n":
        instructions[i] = ("j", b)

    ans = check()

    # swap back
    a, b = instructions[i]
    if a == "j":
        instructions[i] = ("n", b)
    elif a == "n":
        instructions[i] = ("j", b)
    if ans != -1:
        print(ans)
        break
