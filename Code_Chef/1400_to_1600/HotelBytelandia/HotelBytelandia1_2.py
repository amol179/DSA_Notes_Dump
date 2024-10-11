T = int(input())
for _ in range(T):
    N = int(input())
    A = list(input().split())
    D = list(input().split())

    TDA = [[A[i], D[i]] for i in range(len(A))]

    TDA.sort(key=lambda x: x[0])

    print(TDA)

    L = len(TDA)

    entry = []
    guests = 0
    maxguest = 0
    for i in range(L):
        entry.append((TDA[i][0], 1))
        entry.append((TDA[i][1], -1))

    for i in entry:
        guests += i[1]
        maxguest = max(maxguest, guests)

    print(maxguest)
