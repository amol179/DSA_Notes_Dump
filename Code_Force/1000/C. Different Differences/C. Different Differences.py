def max_characteristic_arrays(t, test_cases):
    results = []
    for k, n in test_cases:
        array = []
        current = 1
        increment = 1
        while len(array) < k:
            array.append(current)
            remaining = k - len(array) - 1
            if current + increment + remaining <= n:
                current += increment
                increment += 1
            else:
                current += 1
        results.append(array)
    return results


# Input processing
t = int(input())
test_cases = []
for _ in range(t):
    k, n = map(int, input().split())
    test_cases.append((k, n))

# Get results
results = max_characteristic_arrays(t, test_cases)

# Output results
for res in results:
    print(" ".join(map(str, res)))
