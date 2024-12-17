import sys
import os
from pathlib import Path
import re
from collections import defaultdict

DIR = Path(os.path.dirname(os.path.abspath(__file__)))

file_basename = Path(sys.argv[0]).stem
infile = DIR / "input.txt"
outfile = DIR / f"{file_basename}.txt"

sys.stdin = open(infile, "r")
sys.stdout = open(outfile, "w")


def read_input():
    regA = int(re.findall(r"\d+", input())[0])
    regB = int(re.findall(r"\d+", input())[0])
    regC = int(re.findall(r"\d+", input())[0])

    input()  # empty line

    program = list(map(int, re.findall(r"\d+", input())))

    return {4: regA, 5: regB, 6: regC}, program


def get_reg_char(regs, char):
    if char == "A":
        return regs[4]
    if char == "B":
        return regs[5]
    if char == "C":
        return regs[6]
    raise ValueError


def write_reg_char(regs, char, value):
    if char == "A":
        regs[4] = value
    if char == "B":
        regs[5] = value
    if char == "C":
        regs[6] = value


def as_operand(num, regs):
    if 0 <= num <= 3:
        return num
    return regs[num]


def run(regs, program):
    pc = 0
    output = []
    while pc != len(program):
        inst, opnd = program[pc], program[pc + 1]
        if inst == 0:
            # division
            num = get_reg_char(regs, "A")
            denom = 2 ** as_operand(opnd, regs)
            write_reg_char(regs, "A", num // denom)
        elif inst == 1:
            # xor
            lhs = get_reg_char(regs, "B")
            write_reg_char(regs, "B", lhs ^ opnd)
        elif inst == 2:
            # mod 8
            lhs = as_operand(opnd, regs)
            write_reg_char(regs, "B", lhs % 8)
        elif inst == 3:
            # jump
            regA = get_reg_char(regs, "A")
            if regA != 0:
                pc = opnd - 2  # add 2 later
        elif inst == 4:
            # xor
            regB = get_reg_char(regs, "B")
            regC = get_reg_char(regs, "C")
            write_reg_char(regs, "B", regB ^ regC)
        elif inst == 5:
            # mod 8 + output
            lhs = as_operand(opnd, regs)
            output.append(lhs % 8)
        elif inst == 6:
            # division
            num = get_reg_char(regs, "A")
            denom = 2 ** as_operand(opnd, regs)
            write_reg_char(regs, "B", num // denom)
        elif inst == 7:
            # division
            num = get_reg_char(regs, "A")
            denom = 2 ** as_operand(opnd, regs)
            write_reg_char(regs, "C", num // denom)

        pc += 2

    return output


regs, program = read_input()

# proof by magic:
# first character to print repeats every 64 * 16

start_dig = defaultdict(list)
for i in range(64 * 16):
    regs[4] = i
    output = run(regs, program)[0]
    start_dig[output].append(i)


# no idea how long this will take to run
answers = []


def dfs(start_dig, path, program):
    global answers

    if len(path) == len(program):
        answers.append(path.copy())
        return True

    cur_dig = program[len(path)]
    next_possibilities = start_dig[cur_dig]
    if path:
        next_possibilities = [
            p for p in next_possibilities if p % (2**7) == path[-1] >> 3
        ]

    for p in next_possibilities:
        path.append(p)
        dfs(start_dig, path, program)
        path.pop()
    return False


dfs(start_dig, [], program)


def decode_path(path):
    ret = path[-1] >> 7
    for p in reversed(path):
        ret <<= 3
        ret += p % (2**3)
    return ret


decoded_answers = list(map(decode_path, answers))
decoded_answers.sort()

# 0 proof of correctness for why this works, nor do i know how it works
for p in decoded_answers:
    regs[4] = p
    output = run(regs, program)
    if output == program:
        print(p)
        break
