"""
ID: amolgur1
LANG: PYTHON3
TASK: fence6
"""

def read_input():
    f = open("fence6.in", "r")
    n = int(f.readline().strip())
    segs = {}
    conns = {}
    for _ in range(n):
        s, Ls, N1, N2 = map(int, f.readline().split())
        a = list(map(int, f.readline().split()))
        b = list(map(int, f.readline().split()))
        segs[s] = (Ls, a, b)
        conns[(s, 0)] = a
        conns[(s, 1)] = b
    f.close()
    return n, segs, conns


def build_graph(n, segs, conns):
    endpoint_map = {}
    eid = 0
    for s in segs:
        if (s, 0) not in endpoint_map:
            endpoint_map[(s, 0)] = eid
            eid += 1
        if (s, 1) not in endpoint_map:
            endpoint_map[(s, 1)] = eid
            eid += 1

    def key_for(s, side):
        return tuple(sorted(conns[(s, side)] + [s]))

    groups = {}
    for (s, side) in conns:
        k = key_for(s, side)
        if k not in groups:
            groups[k] = []
        groups[k].append((s, side))

    remap = {}
    new_id = 0
    for group in groups.values():
        for (s, side) in group:
            remap[endpoint_map[(s, side)]] = new_id
        new_id += 1

    V = new_id
    graph = [[] for _ in range(V)]
    edges = []
    for s in segs:
        Ls, _, _ = segs[s]
        u = remap[endpoint_map[(s, 0)]]
        v = remap[endpoint_map[(s, 1)]]
        graph[u].append((v, Ls))
        graph[v].append((u, Ls))
        edges.append((u, v, Ls))
    return V, graph, edges


def shortest_path(V, graph, src, dst, banned):
    INF = 10**9
    dist = [INF] * V
    used = [False] * V
    dist[src] = 0
    for _ in range(V):
        u = -1
        best = INF
        for i in range(V):
            if not used[i] and dist[i] < best:
                best = dist[i]
                u = i
        if u == -1:
            break
        used[u] = True
        for (v, w) in graph[u]:
            if (u, v, w) == banned or (v, u, w) == banned:
                continue
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
    return dist[dst]


def solve():
    n, segs, conns = read_input()
    V, graph, edges = build_graph(n, segs, conns)

    INF = 10**9
    best = INF
    for (u, v, w) in edges:
        d = shortest_path(V, graph, u, v, (u, v, w))
        if d < INF:
            best = min(best, d + w)

    f = open("fence6.out", "w")
    f.write(str(best) + "\n")
    f.close()


if __name__ == "__main__":
    solve()
