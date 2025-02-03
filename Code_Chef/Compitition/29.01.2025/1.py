def count_submatrices(n, m, a, b, grid, k):
    # Compute the prefix sum array with dimensions (n+1) x (m+1)
    prefix = [[0] * (m + 1) for _ in range(n + 1)]
    
    # Fill the prefix sum array
    for i in range(1, n + 1):
        row_sum = 0
        for j in range(1, m + 1):
            row_sum += grid[i - 1][j - 1]
            prefix[i][j] = prefix[i - 1][j] + row_sum
    
    # Variable to store the number of submatrices with at least 'k' ones
    count = 0
    
    # Iterate over all possible positions where the top-left corner of the submatrix can be
    # The submatrix size is 'a x b', so we start from (a, b) to (n, m)
    for i in range(a, n + 1):
        for j in range(b, m + 1):
            # Calculate the number of 1s in the current submatrix using the prefix sum array
            total = prefix[i][j] - prefix[i - a][j] - prefix[i][j - b] + prefix[i - a][j - b]
            
            # Check if the submatrix contains at least 'k' ones
            if total >= k:
                count += 1
    
    return count

# Read input values
n, m, a, b, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Compute and print the result
print(count_submatrices(n, m, a, b, grid, k))
