for _ in range(int(input())):
    A = [int(x) for x in input().split()]
    A.sort()
    count = 0

    for i in range(len(A)):
        if A[i] > 0:
            count += 1
            A[i] -= 1
    if A[0] > 0 and A[1] > 0:
        count += 1
        A[0] -= 1
        A[1] -= 1

    if A[0] > 0 and A[2] > 0:
        count += 1
        A[0] -= 1
        A[2] -= 1

    if A[1] > 0 and A[2] > 0:
        count += 1
        A[1] -= 1
        A[2] -= 1

    print(count)
