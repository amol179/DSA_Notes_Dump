n, m, a = map(int, input().split())
length = (n + a - 1) // a
breath = (m + a - 1) // a
ans = length * breath
print(ans)
