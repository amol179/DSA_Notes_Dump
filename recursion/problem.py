def cut_rod(p, n):
    if n == 0:
        return 0
    q = float('-inf')
    for i in range(1, n+1):
        q = max(q, p[i] + cut_rod(p, n-i))
    print(q)
    return q

prices = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]  # prices for rods of length 0 to 10
rod_length = 8
max_revenue = cut_rod(prices, rod_length)
print("Maximum revenue:", max_revenue)