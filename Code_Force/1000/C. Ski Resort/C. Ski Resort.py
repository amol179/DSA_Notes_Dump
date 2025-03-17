def count_vacation_ways(t, test_cases):
    results = []

    for test in test_cases:
        n, k, q = test[0]
        a = test[1]

        count = 0
        valid_length = 0

        for temp in a + [q + 1]:  # Append a sentinel value greater than q
            if temp <= q:
                valid_length += 1
            else:
                if valid_length >= k:
                    # Count subarrays of length >= k
                    count += (valid_length - k + 1) * (valid_length - k + 2) // 2
                valid_length = 0

        results.append(count)

    return results


# Taking custom input
t = int(input())

test_cases = []
for _ in range(t):
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    test_cases.append([(n, k, q), a])

# Process the test cases
results = count_vacation_ways(t, test_cases)

# Output the results
print()
for res in results:
    print(res)
