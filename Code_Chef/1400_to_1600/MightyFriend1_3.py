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
    i = 0
    j = 0
    while i < len(M) and j < len(T) and M[i] > T[j]:
        for i in range(K):
            M_score = M_score - M[i] + T[j]
            T_score = T_score - T[j] + M[i]
            i += 1
            j += 1

    if T_score > M_score:
        print("Yes")
    else:
        print("NO")
