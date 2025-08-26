t = int(input())
for _ in range(t):
    N, X = map(int, input().split())

    A = []

    if N == 1:
        print(X)

    if N > 1:
        num = N * X
        if N % 2 == 0:
            for i in range(1, N + 1):
                A.append(X + i)
                A.append(X - i)
                if len(A) == N:
                    avg = sum(A) // N
                    break
        else:
            A.append(num)
            for i in range(1, N + 1):
                A.append(i)
                A.append(-i)
                if len(A) == N:
                    break
            avg = sum(A) // N

        print(A)
        print(sum(A))
        print(avg)
