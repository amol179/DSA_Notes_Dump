# isme wrong answer ara hai

for _ in range(int(input())):
    A = []
    N, K = map(int, input().split())

    A = list(map(int, input().split()))
    M = []
    T = []
    for i in range(len(A)):
        if i % 2 == 0:
            M.append(A[i])
        else:
            T.append(A[i])

    M.sort(reverse=True)
    T.sort()

    M_score = sum(M)
    T_score = sum(T)

    i = 0
    j = 0
    while i < len(M) and j < len(T) and M[i] > T[j]:
        M_score = M_score - M[i] + T[j]
        T_score = T_score - T[j] + M[i]
        i += 1
        j += 1

    if T_score > M_score:
        print("Yes")
    else:
        print("NO")
