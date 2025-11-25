"""
ID: amolgur1
LANG: PYTHON3
TASK: cowtour

"""


def cowtour():
    def distance(x1, y1, x2, y2):
        dx = x1 - x2
        dy = y1 - y2
        return (dx * dx + dy * dy) ** 0.5

    with open("cowtour.in", "r") as fin:
        lines = fin.read().splitlines()

    N = int(lines[0])
    coords = []
    for i in range(1, N + 1):
        x, y = map(int, lines[i].split())
        coords.append((x, y))

    adj = lines[N + 1:N + 1 + N]
    INF = 1e20
    dist = [[INF] * N for _ in range(N)]

    # Initialize distances
    for i in range(N):
        dist[i][i] = 0
        for j in range(N):
            if adj[i][j] == '1':
                x1, y1 = coords[i]
                x2, y2 = coords[j]
                dist[i][j] = distance(x1, y1, x2, y2)

    # Floyd-Warshall
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    # Identify connected components (fields)
    visited = [False] * N
    components = []

    def dfs(u, comp):
        visited[u] = True
        comp.append(u)
        for v in range(N):
            if dist[u][v] < INF and not visited[v]:
                dfs(v, comp)

    for i in range(N):
        if not visited[i]:
            comp = []
            dfs(i, comp)
            components.append(comp)

    # Compute max distance from each pasture to others in its field
    max_dist = [0.0] * N
    for i in range(N):
        for j in range(N):
            if dist[i][j] < INF:
                if dist[i][j] > max_dist[i]:
                    max_dist[i] = dist[i][j]

    # Compute diameter of each field
    field_diam = []
    for comp in components:
        diam = 0.0
        for i in comp:
            for j in comp:
                if dist[i][j] < INF and dist[i][j] > diam:
                    diam = dist[i][j]
        field_diam.append(diam)

    # Try all pairs from different fields
    min_diam = INF
    for a in range(len(components)):
        for b in range(a + 1, len(components)):
            for i in components[a]:
                for j in components[b]:
                    d = distance(coords[i][0], coords[i][1], coords[j][0], coords[j][1])
                    new_diam = max(
                        max_dist[i] + d + max_dist[j],
                        field_diam[a],
                        field_diam[b]
                    )
                    if new_diam < min_diam:
                        min_diam = new_diam

    with open("cowtour.out", "w") as fout:
        fout.write("{0:.6f}\n".format(min_diam))

cowtour()