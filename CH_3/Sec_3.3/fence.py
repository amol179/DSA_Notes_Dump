"""
ID: amolgur1
LANG: PYTHON3
TASK: fence
"""


def main():
    fin = open("fence.in", "r")
    data = fin.read().split()
    fin.close()

    F = int(data[0])
    edges = data[1:]
    adj = [[] for _ in range(501)]

    for i in range(0, 2 * F, 2):
        a = int(edges[i])
        b = int(edges[i + 1])
        adj[a].append(b)
        adj[b].append(a)

    for i in range(501):
        adj[i].sort(reverse=True)

    # Find starting point
    start = 501
    for i in range(1, 501):
        if len(adj[i]) % 2 == 1:
            start = min(start, i)
    if start == 501:
        for i in range(1, 501):
            if adj[i]:
                start = i
                break

    # Iterative Hierholzer's algorithm
    stack = [start]
    path = []

    while stack:
        u = stack[-1]
        if adj[u]:
            v = adj[u].pop()
            adj[v].remove(u)
            stack.append(v)
        else:
            path.append(stack.pop())

    fout = open("fence.out", "w")
    for node in reversed(path):
        fout.write(str(node) + "\n")
    fout.close()

main()