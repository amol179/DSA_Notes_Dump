"""
ID: amolgur1
LANG: PYTHON3
TASK: bigbrn
"""

# bigbrn.py

def main():
    fin = open("bigbrn.in", "r")
    fout = open("bigbrn.out", "w")

    N, T = map(int, fin.readline().split())
    trees = set()

    for _ in range(T):
        r, c = map(int, fin.readline().split())
        trees.add((r, c))

    dp = [[0] * (N + 1) for _ in range(N + 1)]
    max_side = 0

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if (i, j) in trees:
                dp[i][j] = 0
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                if dp[i][j] > max_side:
                    max_side = dp[i][j]

    fout.write(str(max_side) + "\n")

    fin.close()
    fout.close()


if __name__ == "__main__":
    main()
