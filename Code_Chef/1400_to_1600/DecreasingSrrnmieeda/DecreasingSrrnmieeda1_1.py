t = int(input())
for _ in range(t):
    L, R = map(int, input().split())
    N = R
    Rem = []
    for i in range(L, R + 1):
        rem = N % L
        L += 1
        Rem.append(rem)
        if rem == 0:
            break

    print(Rem)

    if len(Rem) == 1:
        print("-1")
    else:
        print(L - 1)
