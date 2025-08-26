for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))

    Divisor = A[0]
    for i in range(1, N):
        a, b = Divisor, A[i]
        while b:
            a, b = b, a % b
        Divisor = a
        if Divisor == 1:
            break
    count = 0
    for i in range(N):
        if A[i] != Divisor:
            count += 1
    print(count)
