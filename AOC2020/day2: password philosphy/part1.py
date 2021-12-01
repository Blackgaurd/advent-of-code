import sys
import os

DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(DIR + "/input.txt", "r")
sys.stdout = open(DIR + "/part1.txt", "w")

ans = 0
for line in sys.stdin:
    cnt, char, password = line.split()
    a, b = cnt.split("-")
    if int(a) <= password.count(char[0]) <= int(b):
        ans += 1

print(ans)