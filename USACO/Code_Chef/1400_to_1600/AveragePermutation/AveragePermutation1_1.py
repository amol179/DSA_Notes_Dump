T = int(input())
for _ in range(T):
    N = int(input())

    A = []
    for i in range(1, N + 1):
        A.append(i)

    print(A)

    print(len(A))

    triples = []
    for i in range(len(A) - 2):
        triplet = A[i : i + 3]
        triples.append(triplet)
    print(triples)
