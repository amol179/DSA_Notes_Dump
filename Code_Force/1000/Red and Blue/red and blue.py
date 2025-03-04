def max_prefix_sum(arr):
    max_sum = 0
    current_sum = 0
    for num in arr:
        current_sum += num
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum


def solve(test_cases):
    results = []
    for case in test_cases:
        n, reds, m, blues = case
        max_r = max_prefix_sum(reds)
        max_b = max_prefix_sum(blues)
        results.append(max_r + max_b)
    return results


# Read input data
t = int(input())
test_cases = []
for _ in range(t):
    n = int(input())
    reds = list(map(int, input().split()))
    m = int(input())
    blues = list(map(int, input().split()))
    test_cases.append((n, reds, m, blues))

# Solve each test case and print results
results = solve(test_cases)
for result in results:
    print(result)
