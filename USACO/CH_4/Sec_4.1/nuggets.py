"""
ID: amolgur1
LANG: PYTHON3
TASK:  nuggets
"""

def main():
    # Read input
    with open("nuggets.in", "r") as fin:
        lines = fin.readlines()
        N = int(lines[0])
        sizes = [int(lines[i]) for i in range(1, N + 1)]

    # If any size is 1, all numbers are possible
    if 1 in sizes:
        with open("nuggets.out", "w") as fout:
            fout.write("0\n")
        return

    # Check GCD of all sizes
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    g = sizes[0]
    for s in sizes[1:]:
        g = gcd(g, s)

    if g != 1:
        with open("nuggets.out", "w") as fout:
            fout.write("0\n")
        return

    # DP array to track reachable numbers
    MAX = 65536  # Enough to detect the pattern
    dp = [False] * MAX
    dp[0] = True

    for i in range(MAX):
        if dp[i]:
            for s in sizes:
                if i + s < MAX:
                    dp[i + s] = True

    # Find the largest number that cannot be formed
    max_size = max(sizes)
    count = 0
    result = 0

    for i in range(MAX):
        if dp[i]:
            count += 1
            if count >= max_size:
                break
        else:
            result = i
            count = 0

    with open("nuggets.out", "w") as fout:
        fout.write(str(result) + "\n")

main()