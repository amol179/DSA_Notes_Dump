T = int(input())
for _ in range(T):
    N = int(input())
    A = input()
    S = list(A)
    print(S)
    L = len(S)

    if L <= 1:
        print("Romos")

    if L >= 2:
        for i in range(L - 1):
            if S[i] != S[i + 1]:
                S.remove(S[i] and S[i + 1])
                if i <= 1:
                    print("Zlatan")

            else:
                print("Romos")
