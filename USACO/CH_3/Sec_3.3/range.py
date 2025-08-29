"""
ID: amolgur1
LANG: PYTHON3
TASK:  range
"""
def main():
    # Read input from file
    fin = open("range.in", "r")
    N = int(fin.readline().strip())
    grid = [fin.readline().strip() for _ in range(N)]
    fin.close()

    # Initialize DP table
    dp = [[0] * N for _ in range(N)]
    count = {}

    for i in range(N):
        for j in range(N):
            if grid[i][j] == '1':
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

                # Count squares of size 2 and above
                for size in range(2, dp[i][j] + 1):
                    if size in count:
                        count[size] += 1
                    else:
                        count[size] = 1

    # Write output to file
    fout = open("range.out", "w")
    for size in sorted(count):
        fout.write(str(size) + " " + str(count[size]) + "\n")
    fout.close()

main()