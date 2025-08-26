T = int(input())
for _ in range(T):
    N = int(input())
    A = list(input().split())
    D = list(input().split())

    TDA = [[A[i], D[i]] for i in range(len(A))]

    TDA.sort(key=lambda x: x[0])

    print(TDA)

    L = len(TDA)

    i = 0
    j = 0
    guests = 0
    room = 0
    while i < L:
        if A[i] < D[j]:
            guests += 1
            room = max(room, guests)
            i += 1
        else:
            guests -= 1
            j += 1

    print(room)
