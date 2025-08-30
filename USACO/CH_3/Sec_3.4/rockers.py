"""
ID: amolgur1
LANG: PYTHON3
TASK:  rockers
"""
def main():
    # Read input
    with open("rockers.in", "r") as f:
        N, T, M = map(int, f.readline().strip().split())
        songs = list(map(int, f.readline().strip().split()))

    # Initialize DP table
    dp = [[[0 for _ in range(T + 1)] for _ in range(M + 1)] for _ in range(N + 1)]

    for i in range(N):
        for j in range(M + 1):
            for k in range(T + 1):
                current = dp[i][j][k]

                # Skip the song
                if dp[i + 1][j][k] < current:
                    dp[i + 1][j][k] = current

                # Place on current disk
                if j < M and k + songs[i] <= T:
                    if dp[i + 1][j][k + songs[i]] < current + 1:
                        dp[i + 1][j][k + songs[i]] = current + 1

                # Place on new disk
                if j + 1 < M and songs[i] <= T:
                    if dp[i + 1][j + 1][songs[i]] < current + 1:
                        dp[i + 1][j + 1][songs[i]] = current + 1

    # Find the maximum number of songs
    result = 0
    for j in range(M + 1):
        for k in range(T + 1):
            if dp[N][j][k] > result:
                result = dp[N][j][k]

    # Write output
    with open("rockers.out", "w") as f:
        f.write(str(result) + "\n")

main()