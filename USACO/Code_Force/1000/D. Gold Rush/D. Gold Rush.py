def can_form_m(t, test_cases):
    results = []
    for n, m in test_cases:
        if n < m:
            results.append("NO")
            continue

        stack = [n]
        visited = set()
        found = False

        while stack:
            x = stack.pop()
            if x == m:
                found = True
                break
            if x % 3 == 0 and x not in visited:
                visited.add(x)  # Mark the current pile as visited
                stack.append(x // 3)  # Add smaller pile (x / 3)
                stack.append(2 * x // 3)  # Add larger pile (2 * x / 3)

        results.append("YES" if found else "NO")
    return results


# Input
t = int(input())
test_cases = []
for _ in range(t):
    n, m = map(int, input().split())
    test_cases.append((n, m))

# Process and Output
results = can_form_m(t, test_cases)
print("\n".join(results))
