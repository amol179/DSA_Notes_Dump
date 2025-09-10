"""
ID: amolgur1
LANG: PYTHON3
TASK: buylow

"""

# PROGRAM NAME: buylow

def main():
    fin = open("buylow.in", "r")
    fout = open("buylow.out", "w")

    n = int(fin.readline().strip())
    prices = []
    while len(prices) < n:
        prices.extend(map(int, fin.readline().split()))

    dp = [1] * n
    count = [1] * n

    for i in range(n):
        used_prices = set()
        for j in range(i - 1, -1, -1):
            if prices[j] > prices[i]:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    count[i] = count[j]
                    used_prices = {prices[j]}  # reset with this price
                elif dp[j] + 1 == dp[i]:
                    if prices[j] not in used_prices:
                        count[i] += count[j]
                        used_prices.add(prices[j])

    max_len = max(dp)

    total = 0
    used_prices = set()
    for i in range(n - 1, -1, -1):
        if dp[i] == max_len and prices[i] not in used_prices:
            total += count[i]
            used_prices.add(prices[i])

    fout.write(f"{max_len} {total}\n")
    fout.close()

if __name__ == "__main__":
    main()
