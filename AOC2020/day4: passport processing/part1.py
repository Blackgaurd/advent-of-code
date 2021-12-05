import sys
import os
import re

DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(DIR + "/input.txt", "r")
sys.stdout = open(DIR + "/part1.txt", "w")

arr = [[pair[:3] for pair in re.split(" |\n", i)] for i in sys.stdin.read().split("\n\n")]

ans = 0
for passport in arr:
    for key in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
        if key not in passport:
            break
    else:
        ans += 1

print(ans)
