import sys
import os

DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(f"{DIR}/input.txt", "r")
sys.stdout = open(f"{DIR}/part1.txt", "w")

def parse(line):
    matches = {
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<'
    }
    stack = []
    for char in line:
        if char in "([{<":
            stack.append(char)
        elif stack and stack.pop() != matches[char]:
            return char
    return '.'

scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}
ans = 0
for line in sys.stdin:
    line = line.strip() # remove newline
    result = parse(line)
    if result != '.':
        ans += scores[result]

print(ans)