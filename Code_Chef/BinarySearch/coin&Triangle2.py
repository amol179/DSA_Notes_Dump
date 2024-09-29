for _ in range(int(input())):
    n = int(input())
    c = 0
    total = 0
    i = 1

    while total + i <= n:
        total += i
        c += 1
        i += 1

    print(c)
