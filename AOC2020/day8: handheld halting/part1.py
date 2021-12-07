import sys
import os

DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(DIR + "/input.txt", "r")
sys.stdout = open(DIR + "/part1.txt", "w")

instructions = []
for line in sys.stdin:
    a, b = line.split()
    b = int(b)
    instructions.append((a[0], b))

i = 0
x = 0
completed = [False for _ in range(len(instructions))]
while i < len(instructions):
    if completed[i]:
        print(x)
        break
    a, b = instructions[i]
    completed[i] = True
    if a == 'j':
        i += b
    else:
        i += 1
        if a == 'a':
            x += b
