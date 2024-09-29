t = int(input())
for _ in range(t):
    N, M = map(int, input().split())
    O = N - (N * 0.1)

    if O < M:
        print("Online")
    if O > M:
        print("Dining")
    if O == M:
        print("Either")
