"""
ID: amolgur1
LANG: PYTHON3
TASK: race3

"""
def read_input():
    graph = []
    with open("race3.in", "r") as f:
        while True:
            line = f.readline()
            if line.strip() == "-1":
                break
            parts = list(map(int, line.strip().split()))
            graph.append([x for x in parts if x != -2])
    return graph

def dfs(graph, start, blocked):
    visited = [False] * len(graph)
    stack = [start]
    while stack:
        node = stack.pop()
        if node == blocked or visited[node]:
            continue
        visited[node] = True
        for neighbor in graph[node]:
            stack.append(neighbor)
    return visited

def find_unavoidable(graph):
    unavoidable = []
    for i in range(1, len(graph) - 1):
        visited = dfs(graph, 0, i)
        if not visited[len(graph) - 1]:
            unavoidable.append(i)
    return unavoidable

def find_splitting(graph, unavoidable):
    splitting = []
    for s in unavoidable:
        visited_from_start = dfs(graph, 0, s)
        visited_from_s = dfs(graph, s, -1)

        # Check if any node visited from start (excluding s) is also visited from s
        overlap = False
        for i in range(len(graph)):
            if i != s and visited_from_start[i] and visited_from_s[i]:
                overlap = True
                break
        if not overlap:
            splitting.append(s)
    return splitting

def write_output(unavoidable, splitting):
    with open("race3.out", "w") as f:
        f.write(str(len(unavoidable)))
        for u in unavoidable:
            f.write(" " + str(u))
        f.write("\n")
        f.write(str(len(splitting)))
        for s in splitting:
            f.write(" " + str(s))
        f.write("\n")

def main():
    graph = read_input()
    unavoidable = find_unavoidable(graph)
    splitting = find_splitting(graph, unavoidable)
    write_output(unavoidable, splitting)

main()