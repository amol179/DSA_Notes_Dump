t = int(input())
for _ in range(t):
    N = int(input())

    A = [int(x) for x in input().split()]

    count = 0

    j = 1

    for i in range(2 * N):

        if A[i] <= N:
            print(A[N - j])
            A[i], A[N - j] = A[N - j], A[i]
            j += 1
            count += 1
            print(A)

    print(count)
