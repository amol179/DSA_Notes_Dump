def Game_23(n, m):

    if m % n != 0:
        return -1

    k = m / n

    count2 = count3 = 0

    while k % 2 == 0:
        k /= 2
        count2 += 1
    while k % 3 == 0:
        k /= 3
        count3 += 1

    if k != 1:
        return -1
    else:
        return count2 + count3


n, m = map(int, input().split())

print(Game_23(n, m))
