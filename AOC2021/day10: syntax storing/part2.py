import sys
import os

DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(f"{DIR}/input.txt", "r")
sys.stdout = open(f"{DIR}/part2.txt", "w")

def parse(line):
    matches = {
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<'
    }
    rev_matches = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }
    points = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }
    stack = []
    for char in line:
        if char not in matches:
            stack.append(char)
        elif stack and stack.pop() != matches[char]:
            return 0
    score = 0
    stack.reverse()
    for char in stack:
        score *= 5
        score += points[rev_matches[char]]
    return score

arr = []
for line in sys.stdin:
    parsed = parse(line.strip())
    if parsed:
        arr.append(parsed)
arr.sort()
print(arr[len(arr)//2])
