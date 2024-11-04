for _ in range(int(input())):
    A = [int(x) for x in input().split()]
    A.sort()
    count = 0
    for i in range(len(A) - 1):
        if A[i] == 1:
            count += 1
        if A[i] > 1:
            if A[i] == A[i + 1]:
                count += 2

    print(count)
