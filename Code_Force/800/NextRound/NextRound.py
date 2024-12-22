n, k = map(int, input().split())
count = 0
if n >= k:
    A = [int(x) for x in input().split()]
    for i in range(0, n):
        if A[i] == 0:
            break
        if A[i] >= A[k - 1]:
            count += 1
print(count)
