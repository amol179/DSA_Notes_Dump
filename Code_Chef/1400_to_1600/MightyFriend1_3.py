t = int(input())
for _ in range(t):
    if t >= 1 and t <= 100:
        N, K = map(int, input().split())

    if N >= 1 and N <= 10 ^ 5 and K >= 0 and K <= 10 ^ 5:
        A = list(map(int, input().split()))

        M = sorted(A[0:N:2], reverse=True)
        T = sorted(A[1:N:2])

        for i in range(min(K, len(M), len(T))):
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
