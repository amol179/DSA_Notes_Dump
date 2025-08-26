M, N = map(int, input().split())
if N < 1 or M < 1:
    print("ERROR")

if M <= N and N <= 16:
    A = M * N
    S = A / 2
    print(int(S))
