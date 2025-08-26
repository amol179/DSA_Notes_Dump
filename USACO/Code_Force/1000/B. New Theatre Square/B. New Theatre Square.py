def minimum_paving_cost(testcases):
    results = []

    for testcase in testcases:
        n, m, x, y, grid = testcase
        total_cost = 0

        for row in grid:
            i = 0
            while i < m:
                if row[i] == ".":  # White tile to be paved
                    if (
                        i + 1 < m and row[i + 1] == "." and y < 2 * x
                    ):  # Check for adjacent white tiles and if 1x2 tile is cheaper
                        total_cost += y
                        i += 2  # Skip the next tile as it's already paved
                    else:  # Use 1x1 tile
                        total_cost += x
                        i += 1
                else:
                    i += 1

        results.append(total_cost)

    return results


# Input format
t = int(input())
testcases = []
for _ in range(t):
    n, m, x, y = map(int, input().split())
    grid = [input() for _ in range(n)]
    testcases.append((n, m, x, y, grid))

# Output
results = minimum_paving_cost(testcases)
print()
for result in results:
    print(result)
