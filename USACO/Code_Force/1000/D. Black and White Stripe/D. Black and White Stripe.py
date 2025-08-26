def min_recolorings(t, test_cases):
    results = []
    for case in test_cases:
        n, k, s = case
        # Calculate the number of 'W' in the first window of size k
        current_white_count = s[:k].count("W")
        min_white_count = current_white_count

        # Slide the window across the string
        for i in range(1, n - k + 1):
            # Remove the first character of the previous window and add the new character
            if s[i - 1] == "W":
                current_white_count -= 1
            if s[i + k - 1] == "W":
                current_white_count += 1

            # Update the minimum white count
            min_white_count = min(min_white_count, current_white_count)

        results.append(min_white_count)

    return results


# Input reading
t = int(input())  # Number of test cases
test_cases = []

for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()
    test_cases.append((n, k, s))

# Solve and print results
results = min_recolorings(t, test_cases)
for res in results:
    print(res)
