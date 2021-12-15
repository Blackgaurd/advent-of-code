import sys
import os

DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(f"{DIR}/input.txt", "r")
sys.stdout = open(f"{DIR}/part2.txt", "w")

arr = sys.stdin.read().splitlines()
s = arr[0]
reps = {}
for line in arr[2:]:
    key, char = line.split(" -> ")
    reps[key] = (key[0] + char, char + key[1])

cnt = {}
for i in range(len(s) - 1):
    key = s[i : i + 2]
    if key not in cnt:
        cnt[key] = 0
    cnt[key] += 1


def replace():
    new = {}
    for key, val in list(cnt.items()):
        r1, r2 = reps[key]
        if r1 not in new:
            new[r1] = 0
        if r2 not in new:
            new[r2] = 0
        new[r1] += val
        new[r2] += val
    cnt.clear()
    cnt.update(new)


for i in range(40):
    replace()

letters = {}
for key, val in cnt.items():
    if key[0] not in letters:
        letters[key[0]] = 0
    letters[key[0]] += val

if s[-1] not in letters:
    letters[s[-1]] = 0
letters[s[-1]] += 1

print(max(letters.values()) - min(letters.values()))
