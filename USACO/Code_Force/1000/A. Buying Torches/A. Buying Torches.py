A = []
for _ in range(int(input())):
    x, y, k = map(int, input().split())
    Sticks = (k + k * y) - 1

    extra = x - 1
    Trades = (Sticks + extra - 1) // extra

    ans = k + Trades

    A.append(ans)

for i in A:
    print(i)
