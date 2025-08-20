"""
ID: amolgur1
LANG: PYTHON3
TASK: nocows

"""


MOD = 9901

def solve(N, K):
    # dp[n][h]: exact height = h, g[n][h]: ≤ h
    dp = [[0]*(K+1) for _ in range(N+1)]
    g  = [[0]*(K+1) for _ in range(N+1)]

    # Base: one-node tree has height exactly 1
    dp[1][1] = 1
    for h in range(1, K+1):
        g[1][h] = 1

    # Build heights 2..K
    for h in range(2, K+1):
        for n in range(3, N+1, 2):
            total = 0
            for l in range(1, n-1, 2):
                r = n-1-l
                a = (g[l][h-1] * g[r][h-1]) % MOD
                b = (g[l][h-2] * g[r][h-2]) % MOD
                total = (total + a - b) % MOD
            dp[n][h] = total

        # prefix‐sum into g[*][h]
        for n in range(1, N+1):
            g[n][h] = (g[n][h-1] + dp[n][h]) % MOD

    return dp[N][K] % MOD

with open("nocows.in") as fin:
    N, K = map(int, fin.readline().split())

ans = solve(N, K)

with open("nocows.out", "w") as fout:
    fout.write(str(ans) + "\n")