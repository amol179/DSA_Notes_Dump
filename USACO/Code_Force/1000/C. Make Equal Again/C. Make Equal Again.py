import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    if all(x == a[0] for x in a):
        print(0)
        continue
    # Compute prefix length
    prefix_len = 1
    for i in range(1, n):
        if a[i] == a[0]:
            prefix_len += 1
        else:
            break
    # Compute suffix length
    suffix_len = 1
    for i in range(n - 2, -1, -1):
        if a[i] == a[-1]:
            suffix_len += 1
        else:
            break
    if a[0] == a[-1]:
        res = n - (prefix_len + suffix_len)
        print(max(0, res))
    else:
        print(min(n - prefix_len, n - suffix_len))
