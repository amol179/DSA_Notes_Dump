t = int(input())
for _ in range(t):
    N = int(input())

    A = [int(x) for x in input().split()]

    count = 0

    j = 0

    for i in range(2 * N):

        if A[i] <= N:
            count += i - j

            j += 1

    print(count)
