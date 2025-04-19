n = int(input().strip())
pages = list(map(int, input().split()))
day = 0

while n > 0:
    n = n - pages[day]

    if n <= 0:
        print(day + 1)

    day = (day + 1) % 7
