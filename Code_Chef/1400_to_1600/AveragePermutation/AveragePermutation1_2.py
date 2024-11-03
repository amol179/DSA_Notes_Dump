def permutation(A):
    if len(A) <= 1:
        return [A]
    permutations = []
    for i in range(len(A)):
        current = A[i]
        rem = A[:i] + A[i + 1 :]
        for p in permutation(rem):
            permutations.append([current] + p)
    return permutations


T = int(input())
for _ in range(T):
    N = int(input())

    A = []
    for i in range(1, N + 1):
        A.append(i)

    result = permutation(A)

    print(result)
