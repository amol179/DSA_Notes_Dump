"""
ID: amolgur1
LANG: PYTHON3
TASK: castle
"""


# 5 attemts lage vo bhi 

def read_input(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    M, N = map(int, lines[0].split())
    grid = []
    for i in range(1, N + 1):
        grid.append(list(map(int, lines[i].split())))
    return M, N, grid

DIRS = [('W', 0, -1, 1), ('N', -1, 0, 2), ('E', 0, 1, 4), ('S', 1, 0, 8)]

def bfs(start_i, start_j, room_id, N, M, grid, visited):
    stack = [(start_i, start_j)]
    visited[start_i][start_j] = room_id
    size = 1
    while stack:
        i, j = stack.pop()
        for label, di, dj, bit in DIRS:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M:
                if (grid[i][j] & bit) == 0 and visited[ni][nj] == -1:
                    visited[ni][nj] = room_id
                    size += 1
                    stack.append((ni, nj))
    return size


M, N, grid = read_input('castle.in')
visited = [[-1 for _ in range(M)] for _ in range(N)]
room_sizes = []
room_id = 0

for i in range(N):
    for j in range(M):
        if visited[i][j] == -1:
            room_size = bfs(i, j, room_id, N, M, grid, visited)
            room_sizes.append(room_size)
            room_id += 1

max_merge = 0
best_i = best_j = 0
best_dir = ''

for j in range(M):                    # left to right
    for i in range(N - 1, -1, -1):    # bottom to top
        for dir_label, di, dj, bit in [('N', -1, 0, 2), ('E', 0, 1, 4)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M:
                r1 = visited[i][j]
                r2 = visited[ni][nj]
                if r1 != r2:
                    combined = room_sizes[r1] + room_sizes[r2]
                    if combined > max_merge or (
                        combined == max_merge and (
                            j < best_j or
                            (j == best_j and i > best_i) or
                            (j == best_j and i == best_i and dir_label == 'N')
                        )
                    ):
                        max_merge = combined
                        best_i, best_j, best_dir = i, j, dir_label

with open('castle.out', 'w') as f:
    f.write(f"{room_id}\n")
    f.write(f"{max(room_sizes)}\n")
    f.write(f"{max_merge}\n")
    f.write(f"{best_i + 1} {best_j + 1} {best_dir}\n")