for _ in range(int(input())):
    A = []
    N, K = map(int, input().split())
    M = []
    T = []
    M_score = 0
    T_score = 0

    A = list(map(int, input().split()))

    M = sorted(A[0:N:2], reverse=True)
    T = sorted(A[1:N:2])

    for i in range(K, len(M), len(T)):
        if T[i] < M[i]:
            M[i], T[i] = T[i], M[i]
        else:
            break

    M_score = sum(M)
    T_score = sum(T)

    if T_score > M_score:
        print("Yes")
    else:
        print("NO")
