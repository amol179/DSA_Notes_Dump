"""
ID: amolgur1
LANG: PYTHON3
TASK: stall4
"""

def dfs(cow, visited, match, adj):
    for stall in adj[cow]:
        if not visited[stall]:
            visited[stall] = True
            if match[stall] == -1 or dfs(match[stall], visited, match, adj):
                match[stall] = cow
                return True
    return False

def main():
    # Read input from file
    with open("stall4.in", "r") as f:
        lines = f.readlines()

    N_M = lines[0].split()
    N = int(N_M[0])
    M = int(N_M[1])

    adj = [[] for _ in range(N + 1)]

    for i in range(1, N + 1):
        parts = lines[i].split()
        Si = int(parts[0])
        stalls = list(map(int, parts[1:]))
        adj[i] = stalls

    match = [-1] * (M + 1)
    result = 0

    for cow in range(1, N + 1):
        visited = [False] * (M + 1)
        if dfs(cow, visited, match, adj):
            result += 1

    # Write output to file
    with open("stall4.out", "w") as f:
        f.write(str(result) + "\n")

main()