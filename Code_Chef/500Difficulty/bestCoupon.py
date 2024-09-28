t = int (input())
for _ in range(t):
    A = int (input())
    if A >= 100 and A <= 10000:
        D = A * 0.1
        if D <= 100:
            print(100)
        else:
            print(int(D))