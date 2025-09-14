"""
ID: amolgur1
LANG: PYTHON3
TASK: snail
"""

# snail.py

def parse_position(pos):
    col = ord(pos[0]) - ord('A')
    row = int(pos[1:]) - 1
    return row, col

def dfs(r, c, dr, dc, visited, grid, N):
    max_path = 0
    path = []

    nr, nc = r + dr, c + dc

    # Move in straight line until blocked
    while 0 <= nr < N and 0 <= nc < N and grid[nr][nc] == '.' and not visited[nr][nc]:
        visited[nr][nc] = True
        path.append((nr, nc))
        nr += dr
        nc += dc

    # Step back to last valid cell
    nr -= dr
    nc -= dc

    # Try turning 90 degrees at the end of the run
    for tdr, tdc in [(-dc, dr), (dc, -dr)]:
        tr, tc = nr + tdr, nc + tdc
        if 0 <= tr < N and 0 <= tc < N and grid[tr][tc] == '.' and not visited[tr][tc]:
            max_path = max(max_path, dfs(nr, nc, tdr, tdc, visited, grid, N))

    # Backtrack
    for pr, pc in path:
        visited[pr][pc] = False

    return len(path) + max_path

def main():
    with open("snail.in", "r") as f:
        lines = f.readlines()

    N, B = map(int, lines[0].split())
    grid = [['.' for _ in range(N)] for _ in range(N)]

    for i in range(1, B + 1):
        r, c = parse_position(lines[i].strip())
        grid[r][c] = '#'

    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[0][0] = True

    # Try both initial directions: right and down
    max_squares = max(
        dfs(0, 0, 0, 1, visited, grid, N),
        dfs(0, 0, 1, 0, visited, grid, N)
    ) + 1  # Include starting square

    with open("snail.out", "w") as f:
        f.write(str(max_squares) + "\n")

main()