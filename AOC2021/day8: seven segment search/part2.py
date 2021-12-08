import sys
import os

DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(f"{DIR}/input.txt", "r")
sys.stdout = open(f"{DIR}/part2.txt", "w")

# 1: 2 segments
# 2: 5 segments
# 3: 5 segments
# 4: 4 segments
# 5: 5 segments
# 6: 6 segments
# 7: 3 segments
# 8: 7 segments
# 9: 6 segments
# 0: 6 segments

# segments
#  000
# 1   2
# 1   2
# 1   2
#  333
# 4   5
# 4   5
# 4   5
#  666


def anagrams(a, b):
    return set(a) == set(b)


ttl = 0
for line in sys.stdin:
    segs, out = line.split("|")
    segs = list(map(lambda x: x.strip(), segs.split()))
    out = list(map(lambda x: x.strip(), out.split()))
    ans = ["" for i in range(10)]
    segments = ["" for i in range(7)]

    # take care of obvious cases
    for s in segs:
        if len(s) == 2:
            ans[1] = s
        elif len(s) == 4:
            ans[4] = s
        elif len(s) == 3:
            ans[7] = s
        elif len(s) == 7:
            ans[8] = s

    for char in ans[7]:
        if char not in ans[1]:
            segments[0] = char
            break

    # find out 6
    for s in segs:
        if len(s) == 6 and (ans[1][0] not in s or ans[1][1] not in s):
            ans[6] = s
            if ans[1][0] not in s:
                segments[5] = ans[1][1]
                segments[2] = ans[1][0]
            else:
                segments[5] = ans[1][0]
                segments[2] = ans[1][1]

    # find out 2, 3, 5
    cnt = {char: 0 for char in ans[8]}
    for s in segs:
        if len(s) in [5, 4]:
            for char in s:
                cnt[char] += 1

    for key, val in cnt.items():
        if val == 1:
            segments[4] = key
            break

    for s in segs:
        if len(s) == 5:
            if segments[4] in s:
                ans[2] = s
            elif segments[2] in s:
                ans[3] = s
            else:
                ans[5] = s

    for char in ans[5]:
        if char not in segments and char not in ans[2]:
            segments[1] = char
            break

    # find 0, 9
    for s in segs:
        if len(s) == 6 and s != ans[6]:
            if segments[4] in s:
                ans[0] = s
                for char in s:
                    if char not in segments:
                        segments[6] = char
                        break
            else:
                ans[9] = s

    for i in range(len(segments)):
        if not segments[i]:
            for char in "abcdefg":
                if char not in segments:
                    segments[i] = char
                    break

    # decode numbers
    cur_ttl = ""
    for num in out:
        for i in range(len(ans)):
            if anagrams(ans[i], num):
                cur_ttl += str(i)
                break

    # pprint(ans)
    # pprint(segments)
    # print(cur_ttl)

    ttl += int(cur_ttl)

print(ttl)
