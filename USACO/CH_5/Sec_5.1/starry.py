"""
ID: amolgur1
LANG: PYTHON3
TASK: starry
"""

W = H = 0
sky = []
visited = []
clusters = []
labels = {}
label_char = 'a'

def read_input():
    global W, H, sky, visited
    fin = open("starry.in", "r")
    W = int(fin.readline())
    H = int(fin.readline())
    sky = [list(fin.readline().strip()) for _ in range(H)]
    visited = [[False] * W for _ in range(H)]
    fin.close()

def in_bounds(x, y):
    return 0 <= x < H and 0 <= y < W

def dfs(x, y, cluster, origin):
    visited[x][y] = True
    cluster.append((x - origin[0], y - origin[1]))
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            nx, ny = x + dx, y + dy
            if in_bounds(nx, ny) and not visited[nx][ny] and sky[nx][ny] == '1':
                dfs(nx, ny, cluster, origin)

def transform(shape, op):
    result = []
    for x, y in shape:
        if op == 0: result.append((x, y))
        elif op == 1: result.append((-x, y))
        elif op == 2: result.append((x, -y))
        elif op == 3: result.append((-x, -y))
        elif op == 4: result.append((y, x))
        elif op == 5: result.append((-y, x))
        elif op == 6: result.append((y, -x))
        elif op == 7: result.append((-y, -x))
    return normalize(result)

def normalize(shape):
    min_x = min(x for x, y in shape)
    min_y = min(y for x, y in shape)
    return sorted([(x - min_x, y - min_y) for x, y in shape])

def get_canonical(shape):
    forms = [transform(shape, i) for i in range(8)]
    return min(forms)

def label_cluster(x, y, label):
    stack = [(x, y)]
    sky[x][y] = label
    while stack:
        cx, cy = stack.pop()
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = cx + dx, cy + dy
                if in_bounds(nx, ny) and sky[nx][ny] == '1':
                    sky[nx][ny] = label
                    stack.append((nx, ny))

def process():
    global label_char
    for i in range(H):
        for j in range(W):
            if sky[i][j] == '1' and not visited[i][j]:
                cluster = []
                dfs(i, j, cluster, (i, j))
                canon = tuple(get_canonical(cluster))
                if canon in labels:
                    label = labels[canon]
                else:
                    label = label_char
                    labels[canon] = label
                    label_char = chr(ord(label_char) + 1)
                label_cluster(i, j, label)

def write_output():
    fout = open("starry.out", "w")
    for row in sky:
        fout.write("".join(row) + "\n")
    fout.close()

def main():
    read_input()
    process()
    write_output()

main()