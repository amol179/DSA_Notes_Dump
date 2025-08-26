"""
ID: amolgur1
LANG: PYTHON3
TASK: butter
"""

# butter.py

def read_input(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    N, P, C = map(int, lines[0].split())
    cow_positions = [int(lines[i]) for i in range(1, N + 1)]
    graph = [[] for _ in range(P + 1)]
    for i in range(N + 1, N + C + 1):
        a, b, w = map(int, lines[i].split())
        graph[a].append((b, w))
        graph[b].append((a, w))
    return N, P, cow_positions, graph

def write_output(filename, result):
    with open(filename, 'w') as f:
        f.write(str(result) + '\n')

def push(heap, item):
    heap.append(item)
    i = len(heap) - 1
    while i > 0 and heap[i][0] < heap[(i - 1) // 2][0]:
        heap[i], heap[(i - 1) // 2] = heap[(i - 1) // 2], heap[i]
        i = (i - 1) // 2

def pop(heap):
    if not heap:
        return None
    heap[0], heap[-1] = heap[-1], heap[0]
    item = heap.pop()
    i = 0
    while True:
        left = 2 * i + 1
        right = 2 * i + 2
        smallest = i
        if left < len(heap) and heap[left][0] < heap[smallest][0]:
            smallest = left
        if right < len(heap) and heap[right][0] < heap[smallest][0]:
            smallest = right
        if smallest == i:
            break
        heap[i], heap[smallest] = heap[smallest], heap[i]
        i = smallest
    return item

def dijkstra(start, P, graph):
    dist = [float('inf')] * (P + 1)
    visited = [False] * (P + 1)
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        d, u = pop(heap)
        if visited[u]:
            continue
        visited[u] = True
        for v, w in graph[u]:
            if not visited[v] and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                push(heap, (dist[v], v))
    return dist

def find_best_pasture(N, P, cow_positions, graph):
    cow_count = [0] * (P + 1)
    for pos in cow_positions:
        cow_count[pos] += 1

    total_distance = [0] * (P + 1)

    for cow_pasture in cow_positions:
        dist = dijkstra(cow_pasture, P, graph)
        for i in range(1, P + 1):
            total_distance[i] += dist[i]

    min_total = float('inf')
    for i in range(1, P + 1):
        if total_distance[i] < min_total:
            min_total = total_distance[i]

    return min_total

# Main execution
N, P, cow_positions, graph = read_input('butter.in')
result = find_best_pasture(N, P, cow_positions, graph)
write_output('butter.out', result)