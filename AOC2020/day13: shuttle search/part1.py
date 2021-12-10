import sys
import os

DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(DIR + "/input.txt", "r")
sys.stdout = open(DIR + "/part1.txt", "w")

time = int(input())
arr = filter(lambda x: x != "x", input().split(","))
arr = list(map(int, arr))
x = min(arr, key=lambda x: (time // x + bool(time % x)) * x)
print(((time // x + bool(time % x)) * x - time) * x)
