t = int(input())
for _ in range(t):
    N = int(input())

    A = [int(x) for x in input().split()]

    S = sum(A)
    ans = []
    for i in range(N):
        ans.append((S / (N - 1)) - A[i])

    print(ans)
