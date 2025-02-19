def solve():
    """
    Reads input values X and Y, then determines whether Chef can reach a total of
    at least 100 questions by using up to 10 worksheets (each containing Y questions)
    added to his already answered X questions.

    Input Format:
        A single line with two space-separated integers X and Y.

    Output:
        "YES" if Chef can reach at least 100 questions, otherwise "NO".
    """
    try:
        # Read and parse the input values
        X, Y = map(int, input().strip().split())
    except ValueError:
        # If the input is not in the expected format, exit the function.
        return

    # Calculate the total number of questions Chef can complete.
    total_questions = X + (10 * Y)

    # Check if the total is at least 100 and print the result.
    print("YES" if total_questions >= 100 else "NO")


if __name__ == "__main__":
    solve()
