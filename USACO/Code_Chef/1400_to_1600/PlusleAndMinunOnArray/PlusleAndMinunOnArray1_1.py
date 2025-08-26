for _ in range(int(input())):
    N = int(input())
    A = [int(x) for x in input().split()]
    for i in range(N):
        if i < 0:
            A[i] = -A[i]
    add = sorted([A[i] for i in range(len(A)) if i % 2 == 0])
    minus = sorted([A[i] for i in range(len(A)) if i % 2 != 0])

    if add[0] < minus[0]:
        add[0], minus[0] = minus[0], add[0]
    print(sum(add) - sum(minus))

    print(add)
    print(minus)
