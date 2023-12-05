import sys
import os

DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(DIR + "/input.txt", "r")
sys.stdout = open(DIR + "/part2.txt", "w")


def parse(s):
    if not s:
        return 0
    if s.isdigit():
        return int(s)
    return {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }[s]


ans = 0
for line in sys.stdin.read().splitlines():
    nums = []
    for i in range(len(line)):
        for token in list(map(str, range(1, 10))) + [
            "one",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine",
        ]:
            if line[i:].startswith(token):
                nums.append(token)
                break
    ans += 10 * parse(nums[0]) + parse(nums[-1])

print(ans)
