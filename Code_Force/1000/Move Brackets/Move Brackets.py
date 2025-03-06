def minimum_moves_to_rbs(t, test_cases):
    results = []

    for case in test_cases:
        n, s = case
        balance = 0
        min_moves = 0

        for char in s:
            if char == "(":
                balance += 1
            else:  # char == ')'
                balance -= 1

            if balance < 0:
                min_moves += 1
                balance = 0

        results.append(min_moves)

    return results


# Input reading and function call
if __name__ == "__main__":
    t = int(input())
    test_cases = []

    for _ in range(t):
        n = int(input())
        s = input()
        test_cases.append((n, s))

    # Process each test case
    results = minimum_moves_to_rbs(t, test_cases)

    # Output results
    for res in results:
        print(res)
