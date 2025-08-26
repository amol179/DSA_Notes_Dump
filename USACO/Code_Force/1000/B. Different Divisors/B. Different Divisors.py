def smallest_integer_with_conditions(t, test_cases):
    def find_smallest_a(d):
        # Function to check if a number has at least 4 divisors meeting the conditions
        def has_valid_divisors(n, d):
            divisors = []
            for i in range(1, int(n**0.5) + 1):
                if n % i == 0:
                    divisors.append(i)
                    if i != n // i:
                        divisors.append(n // i)
            divisors.sort()
            if len(divisors) < 4:
                return False
            for j in range(1, len(divisors)):
                if divisors[j] - divisors[j - 1] < d:
                    return False
            return True

        # Iterate until we find the valid number
        current = d * 2
        while True:
            if has_valid_divisors(current, d):
                return current
            current += 1

    results = []
    for d in test_cases:
        results.append(find_smallest_a(d))
    return results


# Input Section
t = int(input())
test_cases = []
for _ in range(t):
    test_cases.append(int(input()))
    print(_)

# Output Section
results = smallest_integer_with_conditions(t, test_cases)
for res in results:
    print(res)
