import sys
import os

DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(DIR + "/input.txt", "r")
sys.stdout = open(DIR + "/part2.txt", "w")

ans = 0
for line in sys.stdin:
    cnt, char, password = line.split()
    a, b = cnt.split("-")
    if (password[int(a)-1] == char[0]) != (password[int(b)-1] == char[0]):
        ans += 1

print(ans)