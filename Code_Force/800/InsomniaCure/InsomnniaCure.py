def count_damaged_dragons(k, l, m, n, d):
    damaged_dragosn = set()
    for i in range(1, d + 1):
        if i % k == 0 or i % l == 0 or i % m == 0 or i % n == 0:
            damaged_dragosn.add(i)

    return len(damaged_dragosn)


k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

result = count_damaged_dragons(k, l, m, n, d)
print(result)
