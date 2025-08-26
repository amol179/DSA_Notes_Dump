"""
ID: amolgur1
LANG: PYTHON3
TASK: money

"""


def count_ways(coins, total):
    dp = [0] * (total + 1)
    dp[0] = 1 
    
    for coin in coins:
        for amt in range(coin, total + 1):
            dp[amt] += dp[amt - coin]
    
    return dp[total]

with open("money.in", "r") as fin:
    lines = fin.readlines()

V_N = lines[0].split()
V = int(V_N[0])
N = int(V_N[1])

coins = []
for line in lines[1:]:
    coins.extend(map(int, line.strip().split()))

result = count_ways(coins, N)

with open("money.out", "w") as fout:
    fout.write(str(result) + "\n")