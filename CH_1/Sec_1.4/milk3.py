"""
ID: amolgur1
LANG: PYTHON3
TASK: milk3
"""

with open("milk3.in", "r") as fin:
    A, B, C = map(int, fin.readline().split())

visited = []
for _ in range(A + 1):
    visited.append([False] * (B + 1))

possible_c_amounts = set()


def pour(a, b, c):
    if visited[a][b]:
        return

    visited[a][b] = True

    if a == 0:
        possible_c_amounts.add(c)

    if a > 0 and b < B:
        amount_to_pour = min(a, B - b)
        pour(a - amount_to_pour, b + amount_to_pour, c)

    if a > 0 and c < C:
        amount_to_pour = min(a, C - c)
        pour(a - amount_to_pour, b, c + amount_to_pour)

    if b > 0 and a < A:
        amount_to_pour = min(b, A - a)
        pour(a + amount_to_pour, b - amount_to_pour, c)

    if b > 0 and c < C:
        amount_to_pour = min(b, C - c)
        pour(a, b - amount_to_pour, c + amount_to_pour)

    if c > 0 and a < A:
        amount_to_pour = min(c, A - a)
        pour(a + amount_to_pour, b, c - amount_to_pour)

    if c > 0 and b < B:
        amount_to_pour = min(c, B - b)
        pour(a, b + amount_to_pour, c - amount_to_pour)


pour(0, 0, C)


with open("milk3.out", "w") as fout:
    fout.write(" ".join(map(str, sorted(possible_c_amounts))) + "\n")
