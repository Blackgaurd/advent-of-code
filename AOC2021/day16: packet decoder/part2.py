# 719244
import sys
import os
from math import ceil
from functools import reduce

DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(f"{DIR}/input.txt", "r")
sys.stdout = open(f"{DIR}/part2.txt", "w")

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


def parse_packet(pad: bool):
    total_length = 6
    version = int(get_next(3), 2)
    typeid = int(get_next(3), 2)
    if typeid == 4:
        value = 0
        while True:
            start = get_next(1)
            value <<= 4
            value += int(get_next(4), 2)
            total_length += 5
            if start == "0":
                break
    else:
        lengthid = get_next(1)
        values = []
        if lengthid == "0":
            num = int(get_next(15), 2)
            total_length += 16 + num
            while True:
                nxt = parse_packet(False)
                num -= nxt[0]
                values.append(nxt[1])
                if num == 0:
                    break
        else:
            num = int(get_next(11), 2)
            total_length += 12
            for _ in range(num):
                nxt = parse_packet(False)
                total_length += nxt[0]
                values.append(nxt[1])
        if typeid == 0:
            value = sum(values)
        elif typeid == 1:
            value = reduce(lambda x, y: x * y, values)
        elif typeid == 2:
            value = min(values)
        elif typeid == 3:
            value = max(values)
        elif typeid == 5:
            value = int(values[0] > values[1])
        elif typeid == 6:
            value = int(values[0] < values[1])
        elif typeid == 7:
            value = int(values[0] == values[1])
    if pad:
        total_length += ceil(ptr / 4) * 4 - ptr
        pad4()
    return total_length, value


ans = parse_packet(True)
print(ans[1])
