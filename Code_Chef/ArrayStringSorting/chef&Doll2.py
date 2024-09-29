t = int(input())
for _ in range(t):
    N = int(input())
    A = []
    for i in range(N):
        A.append(int(input()))
    repeat = {}
    for i in range(len(A)):
        if A[i] in repeat:
            repeat[A[i]] += 1
        else:
            repeat[A[i]] = 1

    for m, n in repeat.items():
        if n % 2 == 1:
            print(m)
