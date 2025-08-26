n, a, b = map(int, input().split())
front = n - a
back = b + 1

print(min(front, back))
