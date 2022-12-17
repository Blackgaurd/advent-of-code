import re
import random

f = open("day16/input.txt", "r")

adj = {}
rates = {}
non_zero = []

valve_p = r"([A-Z]{2})"
rate_p = r"(\d{1,2})"
for line in f:
    v = re.findall(valve_p, line)
    r = re.findall(rate_p, line)
    adj[v[0]] = v[1:]
    rates[v[0]] = int(r[0])
    if int(r[0]) > 0:
        non_zero.append(v[0])

dis = {k: {k: 100 for k in adj} for k in adj}
for k in adj:
    for nxt in adj[k]:
        dis[k][nxt] = 1

for k in adj:
    for i in adj:
        for j in adj:
            dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])


def fitness(perm):
    global dis, rates

    ans = 0
    mins = 30
    path = ["AA"] + perm
    for i in range(1, len(path)):
        cur, nxt = path[i - 1], path[i]
        mins -= dis[cur][nxt]

        if mins < 0:
            break

        mins -= 1
        ans += rates[nxt] * mins

    return ans


# too lazy to think of a smart solution so GAs it is
pop_size = 500
population = []
for i in range(pop_size):
    random.shuffle(non_zero)
    population.append(non_zero.copy())


def fitnesses(pop):
    return [fitness(p) for p in pop]


def selection(pop, fit):
    # 70/30 tournament/elitism

    n = len(pop)

    T_K = 5
    for i in range(n * 7 // 10 // 2):
        inds = random.sample(range(len(pop)), T_K)
        p1 = pop[max(inds, key=lambda x: fit[x])]

        inds = random.sample(range(len(pop)), T_K)
        p2 = pop[max(inds, key=lambda x: fit[x])]
        yield p1, p2

    fp = sorted(zip(fit, pop), key=lambda x: -x[0])
    for i in range(0, n * 3 // 10, 2):
        yield fp[i][1], fp[i + 1][1]


def crossover(p1, p2):
    # pmx crossover for permutation
    map1 = {}
    map2 = {}
    x1, x2 = random.sample(range(len(p1)), 2)
    x1, x2 = min(x1, x2), max(x1, x2)

    c1, c2 = p1.copy(), p2.copy()
    for i in range(x1, x2):
        c1[i] = p2[i]
        map1[p2[i]] = p1[i]

        c2[i] = p1[i]
        map2[p1[i]] = p2[i]

    for i in range(x1):
        while c1[i] in map1:
            c1[i] = map1[c1[i]]
        while c2[i] in map2:
            c2[i] = map2[c2[i]]

    for i in range(x2, len(p1)):
        while c1[i] in map1:
            c1[i] = map1[c1[i]]
        while c2[i] in map2:
            c2[i] = map2[c2[i]]

    return c1, c2


def mutate(p, rate):
    for i in range(len(p)):
        if random.random() > rate:
            continue
        j = random.randint(0, len(p) - 1)
        p[i], p[j] = p[j], p[i]
    return p


def advance(pop):
    fit = fitnesses(pop)

    M_R = 0.1
    new_pop = []
    for p1, p2 in selection(pop, fit):
        c1, c2 = crossover(p1, p2)
        c1 = mutate(c1, M_R)
        c2 = mutate(c2, M_R)
        new_pop.extend([c1, c2])

    return new_pop, max(fit)

max_fit = 0
for i in range(25):
    population, fit = advance(population)
    max_fit = max(max_fit, fit)

print(max_fit)

f.close()
