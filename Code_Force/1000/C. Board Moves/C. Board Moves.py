def min_moves(n):
    # Calculate the number of layers around the middle.
    m = (n - 1) // 2
    # Use a math formula to add up moves from all layers.
    # The formula is: 4 * m * (m + 1) * (2 * m + 1) // 3
    return 4 * m * (m + 1) * (2 * m + 1) // 3


if __name__ == "__main__":
    import sys

    # Read everything from the input.
    input_data = sys.stdin.read().strip().split()
    # The first number tells us how many test boards we have.
    t = int(input_data[0])
    results = []
    # For each test board, calculate the moves.
    for i in range(1, t + 1):
        n = int(input_data[i])
        results.append(str(min_moves(n)))
    # Print out the result for each board.
    sys.stdout.write("\n".join(results))
