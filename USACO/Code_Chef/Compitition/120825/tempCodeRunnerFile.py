def cyclic_rotations(B):
    rotations = []
    M = len(B)
    for i in range(M):
        rotations.append(B[i:] + B[:i])
    return rotations

def find_min_lexicographic_array(T, test_cases):
    results = []
    for t in range(T):
        N, M, A, B = test_cases[t]
        min_lex_A = A[:]
        rotations = cyclic_rotations(B)
        for i in range(N - M + 1):
            for rotation in rotations:
                new_A = A[:i] + rotation + A[i+M:]
                if new_A < min_lex_A:
                    min_lex_A = new_A
        results.append(min_lex_A)
    return results

# Input reading
T = int(input().strip())
test_cases = []
for _ in range(T):
    N, M = map(int, input().strip().split())
    A = list(map(int, input().strip().split()))
    B = list(map(int, input().strip().split()))
    test_cases.append((N, M, A, B))

# Process and output results
results = find_min_lexicographic_array(T, test_cases)
for result in results:
    print(' '.join(map(str, result)))
