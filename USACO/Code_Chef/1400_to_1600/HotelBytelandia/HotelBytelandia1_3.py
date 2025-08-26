T = int(input())
for _ in range(T):
    N = int(input())
    A = list(input().split())
    D = list(input().split())

    A.sort()
    D.sort()
    TDA = [[A[i], D[i]] for i in range(N)]
    print(TDA)

    i = 0
    j = 0
    guests = 0
    room = 0
    while i < len(A) and j < len(D):
        if A[i] < D[j]:
            guests += 1
            room = max(room, guests)
            i += 1
        else:
            guests -= 1
            j += 1

    print(room)
