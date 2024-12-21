n, k = map(int, input().split())
count = 0
if n >= k:
    A = [int(x) for x in input().split()]
    print(A)

    for i in range(len(A) - 1):
        if A[i] >= A[k]:
            count += 1
print(count)
