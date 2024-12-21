T = int(input())
count = 0
for _ in range(T):
    X, Y, Z = map(int, input().split())

    sum = X + Y + Z

    if sum >= 2:
        count += 1

print(count)
