T = int(input())
i = 0
for _ in range(T):
    x = input().strip()

    if x == "++X" or x == "X++":
        i += 1
    if x == "--X" or x == "X--":
        i -= 1
print(i)
