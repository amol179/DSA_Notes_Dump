from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, start):
        visited = set()
        queue = [start]
        result = []

        while queue:
            node = queue.pop(0)
            if node not in visited:
                result.append(node)
                visited.add(node)
                queue.extend(self.graph[node])

        return result


# Example usage:
g = Graph()
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(1, 4)
g.add_edge(3, 4)
g.add_edge(2, 4)
g.add_edge(3, 1)

print("BFS traversal starting from vertex 2:", g.bfs(1))
