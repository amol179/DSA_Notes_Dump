MOD = 10**9 + 7

# DFS to calculate the number of galaxies in a subset of stars
def dfs(stars, visited, i):
    stack = [i]
    visited[i] = True
    while stack:
        idx = stack.pop()
        x, y = stars[idx]
        for j in range(len(stars)):
            if not visited[j]:
                x2, y2 = stars[j]
                if x == x2 or y == y2:  # Same row or column
                    visited[j] = True
                    stack.append(j)

def count_galaxies(stars):
    num_stars = len(stars)
    visited = [False] * num_stars
    galaxies = 0
    for i in range(num_stars):
        if not visited[i]:
            dfs(stars, visited, i)
            galaxies += 1
    return galaxies

# Function to solve each test case
def solve():
    t = int(input())  # Number of test cases
    for _ in range(t):
        n = int(input())  # Size of the matrix
        matrix = [list(map(int, input().strip())) for _ in range(n)]  # Read the matrix

        # Collect all stars (points where a[x][y] == 1)
        stars = []
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == 1:
                    stars.append((i, j))
        
        total_stars = len(stars)
        if total_stars == 0:
            print(0)
            continue

        total_sum = 0
        # Iterate over all subsets of stars using a bitmask approach
        for mask in range(1, 1 << total_stars):  # 1 to 2^total_stars - 1 (non-empty subsets)
            subset = [stars[i] for i in range(total_stars) if (mask & (1 << i)) > 0]
            galaxy_count = count_galaxies(subset)
            total_sum = (total_sum + galaxy_count) % MOD
        
        print(total_sum)

# Main entry point to read input and invoke the solve function
if __name__ == "__main__":
    solve()
