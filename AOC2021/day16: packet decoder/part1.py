import sys
import os
from math import ceil

DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(f"{DIR}/input.txt", "r")
sys.stdout = open(f"{DIR}/part1.txt", "w")

bits = input()


def hex2bin(hexidecimal):
    return "".join(
        "{0:04b}".format(int(hexidecimal[i], 16)) for i in range(len(hexidecimal))
    )


binary = hex2bin(bits)
ptr = 0


def get_next(length):
    global ptr
    if length == 0:
        return ""
    ret = binary[ptr : ptr + length]
    ptr += length
    return ret


def pad4():
    get_next(ceil(ptr / 4) * 4 - ptr)


version_sum = 0


def parse_packet(pad: bool):
    global version_sum
    total_length = 6
    version = int(get_next(3), 2)
    version_sum += version
    typeid = int(get_next(3), 2)
    if typeid == 4:
        while True:
            start = get_next(1)
            num = get_next(4)
            total_length += 5
            if start == "0":
                break
    else:
        lengthid = get_next(1)
        if lengthid == "0":
            num = int(get_next(15), 2)
            total_length += 16 + num
            while True:
                num -= parse_packet(False)
                if num == 0:
                    break
        else:
            num = int(get_next(11), 2)
            total_length += 12
            for _ in range(num):
                total_length += parse_packet(False)
    if pad:
        total_length += ceil(ptr / 4) * 4 - ptr
        pad4()
    return total_length


parse_packet(True)
print(version_sum)
