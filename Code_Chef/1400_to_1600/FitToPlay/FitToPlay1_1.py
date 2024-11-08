t = int(input())
for _ in range(t):
    N = int(input())

    A = [int(x) for x in input().split()]
    max_diff = 0
    for i in range(len(A) - 1):
        Diff = A[i + 1] - A[i]
        if max_diff > Diff:
            max_diff = Diff
            
    print(max_diff)
    
    if ma
