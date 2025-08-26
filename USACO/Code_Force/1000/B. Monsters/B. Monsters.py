t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    monsters = []
    for idx in range(n):
        health = a[idx]
        remainder = health % k
        if remainder == 0:
            remainder = k
        monsters.append((-remainder, idx + 1))  # Negative for descending sort
    monsters.sort()
    print(" ".join(str(m[1]) for m in monsters), end=" \n")
