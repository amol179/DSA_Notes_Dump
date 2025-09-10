"""
ID: amolgur1
LANG: PYTHON3
TASK: ditch
"""
def read_input():
    with open("ditch.in", "r") as f:
        lines = f.readlines()
    N, M = map(int, lines[0].split())
    capacity = [[0] * (M + 1) for _ in range(M + 1)]
    adj = [[] for _ in range(M + 1)]

    for line in lines[1:N+1]:
        u, v, c = map(int, line.split())
        capacity[u][v] += c  # Handle multiple edges
        adj[u].append(v)
        adj[v].append(u)     # Add reverse edge for residual graph

    return N, M, capacity, adj

def bfs(s, t, parent, capacity, flow, adj, M):
    for i in range(M + 1):
        parent[i] = -1
    parent[s] = s
    queue = [(s, float('inf'))]
    front = 0

    while front < len(queue):
        cur, cur_flow = queue[front]
        front += 1
        for next in adj[cur]:
            if parent[next] == -1 and capacity[cur][next] - flow[cur][next] > 0:
                parent[next] = cur
                new_flow = min(cur_flow, capacity[cur][next] - flow[cur][next])
                if next == t:
                    return new_flow
                queue.append((next, new_flow))
    return 0

def edmonds_karp(s, t, capacity, adj, M):
    flow = [[0] * (M + 1) for _ in range(M + 1)]
    parent = [-1] * (M + 1)
    total_flow = 0

    while True:
        new_flow = bfs(s, t, parent, capacity, flow, adj, M)
        if new_flow == 0:
            break
        total_flow += new_flow
        cur = t
        while cur != s:
            prev = parent[cur]
            flow[prev][cur] += new_flow
            flow[cur][prev] -= new_flow
            cur = prev
    return total_flow

def main():
    N, M, capacity, adj = read_input()
    max_flow = edmonds_karp(1, M, capacity, adj, M)
    with open("ditch.out", "w") as f:
        f.write(str(max_flow) + "\n")

main()