def calculate_max_bishop_sums(test_cases):
    results = []
    for t in test_cases:
        n, m, grid = t
        # Create diagonal sum dictionaries
        sum_d1 = {}
        sum_d2 = {}
        for i in range(n):
            for j in range(m):
                d1 = i + j
                d2 = i - j
                sum_d1[d1] = sum_d1.get(d1, 0) + grid[i][j]
                sum_d2[d2] = sum_d2.get(d2, 0) + grid[i][j]

        # Find the maximal sum for each cell
        max_sum = 0
        for i in range(n):
            for j in range(m):
                d1 = i + j
                d2 = i - j
                current_sum = sum_d1[d1] + sum_d2[d2] - grid[i][j]
                max_sum = max(max_sum, current_sum)

        results.append(max_sum)
    return results


# Input Reading
t = int(input())
test_cases = []
for _ in range(t):
    n, m = map(int, input().split())
    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().split())))
    test_cases.append((n, m, grid))

# Process Test Cases
results = calculate_max_bishop_sums(test_cases)
for res in results:
    print(res)
