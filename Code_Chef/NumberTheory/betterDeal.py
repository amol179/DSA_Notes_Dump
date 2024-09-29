t = int(input())
for _ in range(t):
    A, B = map(int, input().split())
    First = round(100 - (100 * (A / 100)))
    Second = round(200 - (200 * (B / 100)))

    if First < Second:
        print("First")
    if First > Second:
        print("Second")
    if First == Second:
        print("Both")
