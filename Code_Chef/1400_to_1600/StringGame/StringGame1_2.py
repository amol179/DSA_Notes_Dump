T = int(input())
for _ in range(T):
    N = int(input())
    A = input()

    S = list(A)
    L = len(S)

    if L <= 1:
        print("Ramos")

    for i in range(L - 1):
        if L <= 1:
            print("Ramos")
        if S[i] != S[i + 1]:
            S.remove(S[i] and S[i + 1])
            if i <= 1:
                print("Zlatan")
                break
        else:
            print("Ramos")
            break
