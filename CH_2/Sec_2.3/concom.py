"""
ID: amolgur1
LANG: PYTHON3
TASK: concom

"""


own = [[0] * 101 for _ in range(101)]
control = [[False] * 101 for _ in range(101)]

    # Read input data
with open('concom.in', 'r') as f:
    n = int(f.readline())
    for _ in range(n):
        i, j, p = map(int, f.readline().split())
        own[i][j] += p

def propagate(i):
    total = [0] * 101  # total shares i holds in each company
    controlled = [False] * 101

        # Initial: i directly owns some shares
    for j in range(1, 101):
        total[j] = own[i][j]

    while True:
        changed = False
        for j in range(1, 101):
            if not controlled[j] and total[j] > 50:
                controlled[j] = True
                changed = True
                    # If i controls j, add j's shares to i's total
                for k in range(1, 101):
                    total[k] += own[j][k]
        if not changed:
            break

    for j in range(1, 101):
        if i != j and controlled[j]:
            control[i][j] = True

    # Run control simulation for each company
for i in range(1, 101):
    propagate(i)

    # Output all control pairs
with open('concom.out', 'w') as f:
    for i in range(1, 101):
        for j in range(1, 101):
            if control[i][j]:
                f.write(f"{i} {j}\n")

