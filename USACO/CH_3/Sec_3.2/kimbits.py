"""
ID: amolgur1
LANG: PYTHON3
TASK: kimbits
"""


def comb(n, k):
    if k < 0 or k > n:
        return 0
    res = 1
    for i in range(1, k + 1):
        res = res * (n - i + 1) // i
    return res

def kimbits(N, L, I):
    result = ""
    for i in range(N):
        count = 0
        for j in range(0, L + 1):
            count += comb(N - i - 1, j)
        if I <= count:
            result += '0'
        else:
            result += '1'
            I -= count
            L -= 1
    return result

# Read input
with open("kimbits.in", "r") as f:
    N, L, I = map(int, f.readline().strip().split())

# Compute result
output = kimbits(N, L, I)

# Write output
with open("kimbits.out", "w") as f:
    f.write(output + "\n")