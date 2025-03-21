def generate_bad_ugly_numbers(t, test_cases):
    results = []

    for n in test_cases:
        if n == 1:
            results.append(-1)  # No solution for single-digit numbers
        else:
            # Create a simple n-digit number which satisfies the condition
            # Example: Start with 2, then append n-1 digits of 3
            s = "2" + "3" * (n - 1)
            results.append(s)

    return results


# Input handling
t = int(input())
test_cases = [int(input()) for _ in range(t)]
results = generate_bad_ugly_numbers(t, test_cases)

# Output results
for res in results:
    print(res)
