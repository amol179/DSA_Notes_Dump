t = int(input())
for _ in range(t):
    N = int(input())

    A = [int(x) for x in input().split()]
    print(A)
    check = []
    count = 0
    left = []
    right = []
    for i in range(len(A)):
        while i < N:
            left.append(A[i])
            if A[i] <= N:
                check.append("T")
            else:
                check.append("F")
            break
        while i >= N:
            right.append(A[i])
            if A[i] <= N:
                check.append("F")
            else:
                check.append("T")
            break
    print(check)
    for i in range(len(left) - 1):
        if check[i] == "F":
            A[i], A[i + 1] = A[i + 1], A[i]
            check[i], check[i + 1] = check[i + 1], check[i]
            count += 1
    print(A)
    print(check)

    for i in range(3, 2 * N - 1):

        if check[i] == "T":
            A[i], A[i + 1] = A[i + 1], A[i]
            check[i], check[i + 1] = check[i + 1], check[i]
            count += 1
    print(A)
    print(check)

    A[N - 1], A[N] = A[N], A[N - 1]
    check[N - 1], check[N] = check[N], check[N - 1]
    count += 1

    print(A)
    print(check)
