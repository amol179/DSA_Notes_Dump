"""
ID: amolgur1
LANG: PYTHON3
TASK: subset
"""




with open("subset.in", "r") as infile:
    N = int(infile.readline().strip())

total = N * (N + 1) // 2

# If total sum is odd, no equal partition is possible
if total % 2 != 0:
    result = 0
else:
    target = total // 2
    dp = [0] * (target + 1)
    dp[0] = 1

    # Dynamic programming to count subset sums
    for i in range(1, N + 1):
        j = target
        while j >= i:
            dp[j] += dp[j - i]
            j -= 1

    # Divide by 2 to avoid double counting symmetric partitions
    result = dp[target] // 2

# Write output to file
with open("subset.out", "w") as outfile:
    outfile.write(str(result) + "\n")