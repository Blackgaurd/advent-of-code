import sys
import os

DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(DIR + "/input.txt", "r")
sys.stdout = open(DIR + "/part2.txt", "w")

arr = sys.stdin.read().split("\n\n")

ans = 0
for group in arr:
    yes = [0 for i in range(26)]
    people = group.split("\n")
    for person in people:
        for char in person:
            if char.isalpha():
                yes[ord(char) - ord("a")] += 1
    ans += yes.count(len(people))

print(ans)
