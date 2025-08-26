def max_difference(t, test_cases):
    results = []

    for case in test_cases:
        n, a, b = case

        # dp[i][0] means Monocarp solves on day i and Stereocarp skips day i
        # dp[i][1] means Monocarp skips day i and Stereocarp solves on day i+1
        dp = [[float("-inf")] * 2 for _ in range(n + 1)]

        # Base case, no days
        dp[0][0] = dp[0][1] = 0

        for i in range(n):
            # Monocarp solves on day i
            dp[i + 1][0] = max(dp[i + 1][0], dp[i][0] + a[i])

            # Stereocarp solves on day i + 1
            if i + 1 < n:
                dp[i + 1][1] = max(dp[i + 1][1], dp[i][0] - b[i + 1])

            # Monocarp skips day i, and nothing for Stereocarp
            dp[i + 1][1] = max(dp[i + 1][1], dp[i][1])

        max_diff = max(dp[n][0], dp[n][1])
        results.append(max_diff)

    return results


# Reading input
t = int(input("Enter the number of test cases: "))
test_cases = []
for _ in range(t):
    n = int(input("Enter the number of days: "))
    a = list(map(int, input(f"Enter {n} integers for Monocarp: ").split()))
    b = list(map(int, input(f"Enter {n} integers for Stereocarp: ").split()))
    test_cases.append((n, a, b))

# Calculate results
results = max_difference(t, test_cases)

# Print results
for result in results:
    print(result)
