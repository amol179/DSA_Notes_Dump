def max_f_of_splits(t, test_cases):
    results = []
    for n, s in test_cases:
        # Track distinct characters for the left and right sides
        left_count = [0] * 26
        right_count = [0] * 26

        # Initialize right side with all characters in the string
        for char in s:
            right_count[ord(char) - ord("a")] += 1

        # Distinct character counts
        left_distinct = 0
        right_distinct = sum(1 for count in right_count if count > 0)

        max_sum = 0

        # Move the split point from 1 to n-1
        for i in range(n):
            char_index = ord(s[i]) - ord("a")

            # Move one character from right to left
            if left_count[char_index] == 0:
                left_distinct += 1
            left_count[char_index] += 1

            if right_count[char_index] == 1:
                right_distinct -= 1
            right_count[char_index] -= 1

            # Compute f(a) + f(b) for this split
            max_sum = max(max_sum, left_distinct + right_distinct)

        results.append(max_sum)

    return results


# Input and Output
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    s = input()
    test_cases.append((n, s))

results = max_f_of_splits(t, test_cases)
for res in results:
    print(res)
