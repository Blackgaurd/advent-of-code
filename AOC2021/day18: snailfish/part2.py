import sys
import os
from pathlib import Path
from dataclasses import dataclass
from typing import Optional
from enum import Enum
from copy import deepcopy

DIR = Path(os.path.dirname(os.path.abspath(__file__)))

file_basename = Path(sys.argv[0]).stem
infile = DIR / "input.txt"
outfile = DIR / f"{file_basename}.txt"

sys.stdin = open(infile, "r")
sys.stdout = open(outfile, "w")


@dataclass
class Number:
    val: int


@dataclass
class Pair:
    left: "Snailfish"
    right: "Snailfish"


Snailfish = Number | Pair


class Direction(Enum):
    LEFT = 1
    RIGHT = 2


def from_string(s: str) -> Snailfish:
    def recur(s: str) -> tuple[Snailfish, str]:
        if s[0] == "[":
            left, rem = recur(s[1:])
            assert rem[0] == ","
            right, rem2 = recur(rem[1:])
            assert rem2[0] == "]"

            return Pair(left, right), rem2[1:]
        else:
            i = 0
            while s[i + 1].isdigit():
                i += 1

            num = int(s[: i + 1])
            return Number(num), s[i + 1 :]

    return recur(s)[0]


def to_string(root: Snailfish) -> str:
    match root:
        case Pair(left, right):
            return f"[{to_string(left)},{to_string(right)}]"
        case Number(x):
            return str(x)


def height(root: Snailfish):
    if isinstance(root, Number):
        return 0
    return 1 + max(height(root.left), height(root.right))


def find_explode(root: Snailfish, depth: int = 1) -> Optional[Pair]:
    if isinstance(root, Number):
        return None

    if isinstance(root.left, Number) and isinstance(root.right, Number) and depth > 4:
        return root

    if ret := find_explode(root.left, depth + 1):
        return ret
    if ret := find_explode(root.right, depth + 1):
        return ret
    return None


def preorder_numbers(root: Snailfish) -> list[Number]:
    if isinstance(root, Number):
        return [root]
    return preorder_numbers(root.left) + preorder_numbers(root.right)


def set_to_zero(root: Snailfish, target: Snailfish):
    if isinstance(root, Number):
        return False

    if root.left is target:
        root.left = Number(0)
        return True

    if root.right is target:
        root.right = Number(0)
        return True

    if not set_to_zero(root.left, target):
        if not set_to_zero(root.right, target):
            return False
    return True


def explode(root: Snailfish) -> bool:
    explode_pair = find_explode(root)
    if explode_pair is None:
        return False

    left_num = explode_pair.left
    right_num = explode_pair.right

    assert isinstance(left_num, Number) and isinstance(right_num, Number)

    nums = preorder_numbers(root)
    for i, num in enumerate(nums):
        if num is left_num and i > 0:
            nums[i - 1].val += left_num.val
        elif num is right_num and i + 1 < len(nums):
            nums[i + 1].val += right_num.val

    set_to_zero(root, explode_pair)

    return True


def split(root: Snailfish) -> bool:
    assert isinstance(root, Pair)

    match root.left:
        case Number(x):
            if x >= 10:
                left_val = x // 2
                right_val = x - left_val
                root.left = Pair(Number(left_val), Number(right_val))
                return True
        case Pair(_, _):
            left_split = split(root.left)
            if left_split:
                return True

    match root.right:
        case Number(x):
            if x >= 10:
                left_val = x // 2
                right_val = x - left_val
                root.right = Pair(Number(left_val), Number(right_val))
                return True
        case Pair(_, _):
            right_split = split(root.right)
            return right_split

    return False


def add(lhs: Snailfish, rhs: Snailfish) -> Snailfish:
    ret = Pair(lhs, rhs)

    while True:
        if explode(ret):
            continue
        if split(ret):
            continue
        break

    return ret


def magnitude(root: Snailfish) -> int:
    match root:
        case Number(x):
            return x
        case Pair(left, right):
            return 3 * magnitude(left) + 2 * magnitude(right)


numbers = list(map(lambda s: from_string(s.strip("\n")), sys.stdin))

ans = 0
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        ans = max(ans, magnitude(add(deepcopy(numbers[i]), deepcopy(numbers[j]))))
        ans = max(ans, magnitude(add(deepcopy(numbers[j]), deepcopy(numbers[i]))))

print(ans)
