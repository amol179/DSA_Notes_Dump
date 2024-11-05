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

    a = max(left)
    b = min(right)

    print(a, b)

    if a > b:
        a, b = b, a

    print(a, b)
