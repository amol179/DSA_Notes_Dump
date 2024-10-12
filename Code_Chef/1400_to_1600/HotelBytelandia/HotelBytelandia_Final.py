T = int(input())
for _ in range(T):
    N = int(input())
    A = [int(i) for i in input().split()]
    D = [int(i) for i in input().split()]

    maxR = 0
    Guests = 0
    for i in range(1, max(D) + 1):
        # (1, max(D) + 1) D ki maximum value tk he loop krenga,
        # +1 isliye q ki last index ko include nahi krta
        while i in A:
            Guests += 1
            A.remove(i)
        while i in D:
            Guests -= 1
            D.remove(i)
        maxR = max(maxR, Guests)

    print(maxR)
