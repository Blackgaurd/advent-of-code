# Chinese Remainder Theorem :weary:

import sys
import os
from functools import reduce

DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(DIR + "/input.txt", "r")
sys.stdout = open(DIR + "/part2.txt", "w")

input()
arr = input().split(",")

a = []
n = []
for i in range(len(arr)):
    if arr[i] != "x":
        a.append(i)
        n.append(int(arr[i]))
for i in range(len(a)):
    a[i] = n[i] - a[i]


def extended_euclid(a, b):
    if b == 0:
        return (1, 0)
    x, y = extended_euclid(b, a % b)
    k = a // b
    return y, x - k * y


def inverse_mod(a, m):
    b, _ = extended_euclid(a, m)
    if b < 0:
        b = (b % m + m) % m
    return b


def crt(a, n):
    # a = congruences
    # n = mods
    N = reduce(lambda x, y: x * y, n)
    y = [N // i for i in n]
    z = [inverse_mod(i, j) for i, j in zip(y, n)]
    return sum(a[i] * y[i] * z[i] for i in range(len(a))) % N


start_time = crt(a, n)

print(start_time)
