"""
ID: amolgur1
LANG: PYTHON3
TASK:  game1
"""

def main():
    # Read input from file
    fin = open("game1.in", "r")
    N = int(fin.readline().strip())
    board = []
    while len(board) < N:
        board += list(map(int, fin.readline().strip().split()))
    fin.close()

    # Precompute prefix sums for quick range total
    prefix = [0] * (N + 1)
    for i in range(N):
        prefix[i + 1] = prefix[i] + board[i]

    def total(i, j):
        return prefix[j + 1] - prefix[i]

    # dp[i][j] = max score current player can get from board[i..j]
    dp = [[0] * N for _ in range(N)]

    for length in range(1, N + 1):
        for i in range(N - length + 1):
            j = i + length - 1
            if i == j:
                dp[i][j] = board[i]
            else:
                pick_left = board[i] + total(i + 1, j) - dp[i + 1][j]
                pick_right = board[j] + total(i, j - 1) - dp[i][j - 1]
                dp[i][j] = max(pick_left, pick_right)

    player1 = dp[0][N - 1]
    player2 = total(0, N - 1) - player1

    # Write output to file
    fout = open("game1.out", "w")
    fout.write(str(player1) + " " + str(player2) + "\n")
    fout.close()

main()