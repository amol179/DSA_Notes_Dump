def minimum_cost_to_zero(t, test_cases):
    results = []
    for case in test_cases:
        x, y, a, b = case
        # Calculate costs
        cost_individual = (abs(x) + abs(y)) * a
        cost_combined = min(abs(x), abs(y)) * b + abs(abs(x) - abs(y)) * a
        # Get the minimum cost
        results.append(min(cost_individual, cost_combined))
    return results


# Read input
t = int(input())
test_cases = []
for _ in range(t):
    x, y = map(int, input().split())
    a, b = map(int, input().split())
    test_cases.append((x, y, a, b))

# Get results
results = minimum_cost_to_zero(t, test_cases)

# Print results
print()
for result in results:
    print(result)
