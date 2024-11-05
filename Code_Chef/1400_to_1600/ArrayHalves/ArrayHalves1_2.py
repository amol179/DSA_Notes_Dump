t = int(input())
for _ in range(t):
    N = int(input())

    A = [int(x) for x in input().split()]
    print(A)
    left = []
    right = []
    for i in range(len(A)):
        while i < N:
            left.append(A[i])
            break
        while i >= N:
            right.append(A[i])
            break
    print(left)
    print(right)

    count = 0

    for i in range(N):
        if left[i] > right[i]:
            left[i], right[i] = right[i], left[i]
            count += 1
    print(left)
    print(right)

    print(count)
