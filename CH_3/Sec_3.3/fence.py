"""
ID: amolgur1
LANG: PYTHON3
TASK: fence
"""


def dfs(u, adj, path):
    while adj[u]:
        v = adj[u].pop()
        adj[v].remove(u)
        dfs(v, adj, path)
    path.append(u)

def main():
    with open("fence.in", "r") as fin:
        lines = fin.readlines()

    F = int(lines[0])
    adj = [[] for _ in range(501)]

    for line in lines[1:F+1]:
        a, b = map(int, line.strip().split())
        adj[a].append(b)
        adj[b].append(a)

    # Sort adjacency lists in reverse for efficient pop from end
    for i in range(501):
        adj[i].sort(reverse=True)

    # Find starting point: smallest odd-degree node or smallest node with edges
    start = 501
    for i in range(1, 501):
        if len(adj[i]) % 2 == 1:
            start = min(start, i)
    if start == 501:
        for i in range(1, 501):
            if adj[i]:
                start = i
                break

    path = []
    dfs(start, adj, path)

    with open("fence.out", "w") as fout:
        for node in reversed(path):
            fout.write(str(node) + "\n")

main()