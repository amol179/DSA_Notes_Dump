T = int(input())
for _ in range(T):
    N, M = map(int, input().split())

    while M != 0:
        N, M = M, N % M

    print(N)
