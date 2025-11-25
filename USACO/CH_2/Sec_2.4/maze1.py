"""
ID: amolgur1
LANG: PYTHON3
TASK: maze1
"""


def main():
    with open('maze1.in', 'r') as f:
        first_line = f.readline().strip()
        W, H = map(int, first_line.split())
        maze = [list(f.readline().rstrip('\n')) for _ in range(2 * H + 1)]

    # Convert wall format to cell graph
    def get_neighbors(x, y):
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        moves = []
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            wall_x = x * 2 + 1 + dx
            wall_y = y * 2 + 1 + dy
            if 0 <= nx < H and 0 <= ny < W:
                if maze[wall_x][wall_y] == ' ':
                    moves.append((nx, ny))
        return moves

    # Find all exit points
    exits = []
    for i in range(W):
        if maze[0][2 * i + 1] == ' ':
            exits.append((0, i))
        if maze[2 * H][2 * i + 1] == ' ':
            exits.append((H - 1, i))
    for i in range(H):
        if maze[2 * i + 1][0] == ' ':
            exits.append((i, 0))
        if maze[2 * i + 1][2 * W] == ' ':
            exits.append((i, W - 1))

    # BFS from multiple sources
    visited = [[-1 for _ in range(W)] for _ in range(H)]
    queue = []
    for x, y in exits:
        visited[x][y] = 1
        queue.append((x, y))

    head = 0
    while head < len(queue):
        x, y = queue[head]
        head += 1
        for nx, ny in get_neighbors(x, y):
            if visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))

    # Find worst case distance
    max_dist = 0
    for row in visited:
        max_dist = max(max_dist, max(row))

    with open('maze1.out', 'w') as f:
        f.write(str(max_dist) + '\n')

main()