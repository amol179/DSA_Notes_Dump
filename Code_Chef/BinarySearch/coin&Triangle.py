for _ in range(int(input())):
    i = 1
    c = 0
    n = int(input())
    for i in range(1, n + 1):
        i = i * (i + 1) / 2
        if i > n:
            break
        else:
            c += 1
    print(c)
