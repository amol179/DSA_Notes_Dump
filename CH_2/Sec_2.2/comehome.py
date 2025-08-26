"""
ID: amolgur1
LANG: PYTHON3
TASK: comehome
"""


def dijkstra(graph, start):
    nodes = list(graph.keys())
    distances = {}
    for node in nodes:
        distances[node] = 1000000000  # large number instead of float('inf')
    distances[start] = 0

    visited = {}
    for node in nodes:
        visited[node] = False

    queue = [start]

    while queue:
        # Find unvisited node with smallest distance
        min_dist = 1000000000
        min_node = ''
        for node in queue:
            if not visited[node] and distances[node] < min_dist:
                min_dist = distances[node]
                min_node = node

        if min_node == '':
            break

        visited[min_node] = True
        queue.remove(min_node)

        for neighbor, weight in graph[min_node]:
            if distances[neighbor] > distances[min_node] + weight:
                distances[neighbor] = distances[min_node] + weight
                if not visited[neighbor]:
                    queue.append(neighbor)

    return distances

def main():
    with open("comehome.in", "r") as f:
        lines = f.readlines()

    P = int(lines[0].strip())
    graph = {}

    for i in range(1, P + 1):
        a, b, d = lines[i].strip().split()
        d = int(d)
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []
        graph[a].append((b, d))
        graph[b].append((a, d))

    distances = dijkstra(graph, 'Z')

    min_dist = 1000000000
    fastest_cow = ''
    for node in graph:
        if node != 'Z' and 'A' <= node <= 'Y':
            if distances[node] < min_dist:
                min_dist = distances[node]
                fastest_cow = node

    with open("comehome.out", "w") as f:
        f.write(f"{fastest_cow} {min_dist}\n")

main()
