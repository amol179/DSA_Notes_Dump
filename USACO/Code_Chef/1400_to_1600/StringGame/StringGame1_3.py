T = int(input())
for _ in range(T):
    N = int(input())
    A = input()

    S = list(A)

    print(S)

    a = 0
    b = 0

    for i in range(len(S)):

        if S[i] == "1":
            a += 1

        if S[i] == "0":
            b += 1

    print("a ", a)
    print("b ", b)

    if a == b:
        if a % 2 == 0:
            print("Ramus")
        else:
            print("Zlatan")
    elif a < b:
        if a == 0:
            print("Ramus")
        elif a != 0:
            if a % 2 == 0:
                print("Ramus")
            else:
                print("Zlatan")
        else:
            print("Zlatan")
    elif a > b:
        if b == 0:
            print("Ramus")
        elif b != 0:
            if b % 2 == 0:
                print("Ramus")
            else:
                print("Zlatan")
