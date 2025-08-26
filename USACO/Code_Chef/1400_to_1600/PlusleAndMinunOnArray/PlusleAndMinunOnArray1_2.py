for _ in range(int(input())):
    N = int(input())
    A = [int(x) for x in input().split()]
    for i in range(N):
        A[i] = abs(A[i])
    add = sorted(A[::2])
    minus = sorted(A[1::2], reverse=True)
    if add[0] < minus[0]:
        add[0], minus[0] = minus[0], add[0]
    print(sum(add) - sum(minus))
