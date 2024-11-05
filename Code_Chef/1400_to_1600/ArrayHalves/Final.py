t = int(input())
for _ in range(t):
    N = int(input())

    A = [int(x) for x in input().split()]

    count = 0

    left = []
    right = []
    for i in range(N + 1):
        if A[i] > A[i + 1]:
            A[i], A[i + 1] = A[i + 1], A[i]
            count += 1

    print(A)
    print(count)
