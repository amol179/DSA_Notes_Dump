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

    def dfs_util(self, node, visited, result):
        visited.add(node)
        result.append(node)
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self.dfs_util(neighbor, visited, result)

    def dfs(self, start):
        visited = set()
        result = []
        self.dfs_util(start, visited, result)
        return result

# Example usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("BFS traversal starting from vertex 2:", g.bfs(2))
print("DFS traversal starting from vertex 2:", g.dfs(2))
