import sys
import os
import re

DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(DIR + "/input.txt", "r")
sys.stdout = open(DIR + "/part2.txt", "w")

arr = [
    dict([pair.split(":") for pair in re.split(" |\n", i)])
    for i in sys.stdin.read().split("\n\n")
]

ans = 0
for passport in arr:
    for key in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
        if key not in passport:
            break
    else:
        hgt_condition = False
        if passport["hgt"].endswith("cm"):
            hgt_condition = 150 <= int(passport["hgt"][:-2]) <= 193
        elif passport["hgt"].endswith("in"):
            hgt_condition = 59 <= int(passport["hgt"][:-2]) <= 76
        if all(
            [
                hgt_condition,
                1920 <= int(passport["byr"]) <= 2002,
                2010 <= int(passport["iyr"]) <= 2020,
                2020 <= int(passport["eyr"]) <= 2030,
                re.match("#[a-f0-9]{6}$", passport["hcl"]),
                passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
                passport["pid"].isdigit(),
                len(passport["pid"]) == 9,
            ]
        ):
            ans += 1

print(ans)
