from functools import cmp_to_key

f = open("day13/input.txt", "r")

lines = f.readlines()
parse_iter = zip(*[map(lambda x: x.rstrip("\n").strip(), lines)] * 3)


def compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        if a < b:
            return 1
        elif a > b:
            return -1
        return 0
    elif isinstance(a, int):
        a = [a]
    elif isinstance(b, int):
        b = [b]

    for i in range(min(len(a), len(b))):
        comp = compare(a[i], b[i])
        if comp != 0:
            return comp

    if len(a) < len(b):
        return 1
    elif len(a) > len(b):
        return -1
    return 0


lists = []
for i, group in enumerate(parse_iter, start=1):
    a = group[0]
    b = group[1]

    lists.extend([a, b])

lists.append("[[2]]")
lists.append("[[6]]")


# convert to str because stupid python reference equality
lists = list(map(str, lists))
lists.sort(key=cmp_to_key(lambda a, b: compare(eval(a), eval(b))), reverse=True)

ans = 1
for i, lst in enumerate(lists, start=1):
    if lst == "[[6]]" or lst == "[[2]]":
        ans *= i

print(ans)

f.close()
