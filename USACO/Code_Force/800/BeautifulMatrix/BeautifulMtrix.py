# Initialize the matrix
matrix = []

# Read the matrix input
for i in range(5):
    row = list(map(int, input().split()))
    matrix.append(row)

# Find the position of '1'
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            # Calculate the number of moves to bring '1' to the center (2,2)
            moves = abs(i - 2) + abs(j - 2)
            print(moves)
            break
