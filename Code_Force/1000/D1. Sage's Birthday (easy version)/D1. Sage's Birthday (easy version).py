def maximize_cheap_spheres(n, prices):
    # Step 1: Sort the prices in ascending order
    prices.sort()

    # Step 2: Create a new array to reorder the prices
    reordered = [0] * n

    # Place the smaller half of prices into odd indices (1-based)
    odd_indices = range(1, n, 2)
    for i, idx in enumerate(odd_indices):
        reordered[idx] = prices[i]

    # Place the larger half of prices into even indices (1-based)
    even_indices = range(0, n, 2)
    for i, idx in enumerate(even_indices):
        reordered[idx] = prices[len(odd_indices) + i]

    # Count the number of cheap spheres
    cheap_count = 0
    for i in range(1, n - 1):
        if reordered[i] < reordered[i - 1] and reordered[i] < reordered[i + 1]:
            cheap_count += 1

    return cheap_count, reordered


# Input
n = int(input())
prices = list(map(int, input().split()))

# Output
cheap_count, reordered_prices = maximize_cheap_spheres(n, prices)
print(cheap_count)
print(" ".join(map(str, reordered_prices)))
