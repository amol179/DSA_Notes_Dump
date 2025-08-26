"""
ID: amolgur1
LANG: PYTHON3
TASK: ttwo


"""

# Directions: 0 = North, 1 = East, 2 = South, 3 = West
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def move(x, y, d, grid):
    nx = x + dx[d]
    ny = y + dy[d]
    if 0 <= nx < 10 and 0 <= ny < 10 and grid[nx][ny] != '*':
        return nx, ny, d
    else:
        return x, y, (d + 1) % 4

with open('ttwo.in', 'r') as fin:
    grid = [list(fin.readline().strip()) for _ in range(10)]

# Initialize positions and directions
for i in range(10):
    for j in range(10):
        if grid[i][j] == 'F':
            fx, fy = i, j
        elif grid[i][j] == 'C':
            cx, cy = i, j

fd, cd = 0, 0  # both start facing north
visited = [[[[[[False for _ in range(4)] for _ in range(10)] for _ in range(10)]
              for _ in range(4)] for _ in range(10)] for _ in range(10)]

minutes = 0
while True:
    if fx == cx and fy == cy:
        break
    if visited[fx][fy][fd][cx][cy][cd]:
        minutes = 0
        break
    visited[fx][fy][fd][cx][cy][cd] = True
    fx, fy, fd = move(fx, fy, fd, grid)
    cx, cy, cd = move(cx, cy, cd, grid)
    minutes += 1
    if minutes > 160000:  # max possible states
        minutes = 0
        break

with open('ttwo.out', 'w') as fout:
    fout.write(str(minutes) + '\n')