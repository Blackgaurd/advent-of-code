import os
import sys

DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(f"{DIR}/input.txt", "r")
sys.stdout = open(f"{DIR}/part1.txt", "w")


def tokenize(line):
    for token in line.split():
        if len(token) == 1:
            yield token
        else:
            yield from token


def solve(line):
    stack = []
    for char in tokenize(line):
        if not stack:
            if char.isdigit():
                stack.append(int(char))
            else:
                stack.append(char)
        elif char.isdigit():
            op = stack[-1]
            if op == "+":
                stack.pop()
                stack.append(stack.pop() + int(char))
            elif op == "*":
                stack.pop()
                stack.append(stack.pop() * int(char))
            else:
                stack.append(int(char))
        elif char in "+*(":
            stack.append(char)
        else:
            num = stack.pop()
            stack.pop()
            op2 = stack[-1] if stack else None
            if op2 == "+":
                stack.pop()
                stack.append(stack.pop() + num)
            elif op2 == "*":
                stack.pop()
                stack.append(stack.pop() * num)
            else:
                stack.append(num)
    return stack[0]

ans = sum(solve(line) for line in sys.stdin.read().splitlines())
print(ans)
