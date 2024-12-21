T = int(input())
for _ in range(T):
    S = list(input())
    L = len(S)
    if L <= 10:
        print(L)
    if L > 10:
        print(S[0] + str(L - 2) + S[-1])
