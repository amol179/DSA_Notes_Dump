def can_crack_password(t, test_cases):
    results = []

    for n, a, b in test_cases:
        possible = True
        ones_a = ones_b = 0

        for i in range(n):
            if a[i] == "1":
                ones_a += 1
            if b[i] == "1":
                ones_b += 1

            # up to index i, check if we can swap freely
            if ones_a == ones_b:
                continue
            else:
                # if mismatch and the number of 1s so far doesn't match, check the current bit
                if a[i] != b[i]:
                    possible = False
                    break

        results.append("YES" if possible else "NO")

    return results


# Reading input
t = int(input())
test_cases = []


for _ in range(t):
    n = int(input())
    a = input().strip()
    b = input().strip()

    test_cases.append((n, a, b))

# Running the function
results = can_crack_password(t, test_cases)

# Output
for res in results:
    print(res)
