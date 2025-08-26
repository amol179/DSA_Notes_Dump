"""
ID: amolgur1
LANG: PYTHON3
TASK: agrinet

"""
def read_input(filename):
    with open(filename, 'r') as f:
        lines = f.read().split()
        N = int(lines[0])
        matrix = []
        index = 1
        for i in range(N):
            row = []
            for j in range(N):
                row.append(int(lines[index]))
                index += 1
            matrix.append(row)
        return N, matrix

def write_output(filename, result):
    with open(filename, 'w') as f:
        f.write(str(result) + '\n')

def prim(N, matrix):
    visited = [False] * N
    dist = [100001] * N  # max distance is 100000
    dist[0] = 0
    total = 0

    for _ in range(N):
        min_dist = 100001
        u = -1
        for i in range(N):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                u = i
        visited[u] = True
        total += min_dist
        for v in range(N):
            if not visited[v] and matrix[u][v] < dist[v]:
                dist[v] = matrix[u][v]
    return total

def main():
    N, matrix = read_input('agrinet.in')
    result = prim(N, matrix)
    write_output('agrinet.out', result)

main()
