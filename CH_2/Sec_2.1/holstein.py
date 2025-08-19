"""
ID: amolgur1
LANG: PYTHON3
TASK: holstein
"""

# 3 attempts, meri galti. vitamins ko and types ko samjha nahi achese 

def is_valid(combination, feed_vitamins, requirements, V):
    total = [0] * V
    for idx in combination:
        for i in range(V):
            total[i] += feed_vitamins[idx][i]
    return all(total[i] >= requirements[i] for i in range(V))

def dfs(current, selected, V, G, requirements, feed_vitamins, best):
    if is_valid(selected, feed_vitamins, requirements, V):
        if len(selected) < len(best[0]) or (len(selected) == len(best[0]) and selected < best[0]):
            best[0] = selected[:]
        return
    for i in range(current, G):
        selected.append(i)
        dfs(i + 1, selected, V, G, requirements, feed_vitamins, best)
        selected.pop()

def holstein_solver(V, requirements, G, feed_vitamins):
    best = [[i for i in range(G)]]
    dfs(0, [], V, G, requirements, feed_vitamins, best)
    return [len(best[0])] + [i + 1 for i in best[0]]


with open("holstein.in", "r") as f:
    V = int(f.readline().strip())
    requirements = list(map(int, f.readline().strip().split()))
    G = int(f.readline().strip())
    feed_vitamins = []
    for _ in range(G):
        feed_vitamins.append(list(map(int, f.readline().strip().split())))

result = holstein_solver(V, requirements, G, feed_vitamins)

with open("holstein.out", "w") as f:
    f.write(" ".join(map(str, result)) + "\n")
