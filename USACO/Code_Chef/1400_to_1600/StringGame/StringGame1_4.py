T = int(input())
for _ in range(T):
    N = int(input())

    A = input()

    S = list(A)

    print(S)

    count = 0

    i = 0
    while i < len(S) - 1:
        if S[i] != S[i + 1]:
            del S[i : i + 2]
            i = 0
            count += 1
        else:
            i += 1

    print(count)

    if count % 2 == 0:
        print("Ramos")
    else:
        print("Zlatan")
