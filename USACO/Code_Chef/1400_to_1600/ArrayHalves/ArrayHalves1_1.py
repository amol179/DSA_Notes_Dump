t = int(input())
for _ in range(t):
    N = int(input())

    A = [int(x) for x in input().split()]

    i = 1
    for i in range(N):
        if A[i] > A[-i]:
            A[i], A[-i] = A[-i], A[i]

    print(A)
