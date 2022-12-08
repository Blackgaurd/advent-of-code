f = open("day7/input.txt", "r")

crumbs = ["/"]
seen = set()
parse_ls = True
adj = {"/": {"size": 0, "children": set()}}
for line in map(lambda x: x.rstrip("\n"), f.readlines()):
    if line.startswith("$"):
        args = line.split()[1:]
        if args[0] == "cd":
            if args[1] == "..":
                crumbs.pop()
            elif args[1] == "/":
                crumbs = ["/"]
            else:
                cur = ".".join(crumbs)
                new_dir = f"{cur}.{args[1]}"
                crumbs.append(args[1])
                if new_dir not in adj:
                    adj[new_dir] = {"size": 0, "children": set()}
                adj[cur]["children"].add(new_dir)
            parse_ls = True
    elif not line.startswith("dir"):
        cur = ".".join(crumbs)
        adj[cur]["size"] += int(line.split()[0])

dp = {}

def get_size(cur):
    ret = adj[cur]["size"]
    for child in adj[cur]["children"]:
        ret += get_size(child)
    dp[cur] = ret
    return ret

get_size("/")
needed = 30000000 - (70000000 - dp["/"])
possible = []
for key, val in dp.items():
    if val >= needed:
        possible.append(val)
print(min(possible))

f.close()