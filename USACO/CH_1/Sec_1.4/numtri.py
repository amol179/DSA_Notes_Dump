"""
ID: amolgur1
LANG: PYTHON3
TASK:numtri
"""
# 1st attempt


with open("numtri.in", "r") as f:
    R = int(f.readline())
    triangle = [list(map(int, f.readline().split())) for _ in range(R)]

for row in range(R - 2, -1, -1):
    for col in range(len(triangle[row])):
        triangle[row][col] += max(triangle[row + 1][col], triangle[row + 1][col + 1])
with open("numtri.out", "w") as f:
    f.write(str(triangle[0][0]) + "\n")
