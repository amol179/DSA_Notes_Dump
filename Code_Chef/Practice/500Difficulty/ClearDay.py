x, y = map(int, input().strip().split())
if x + y <= 7:
    clearD = 7 - (x+y)
    print(clearD)