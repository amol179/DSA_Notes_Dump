"""
ID: amolgur1
LANG: PYTHON3
TASK: transform
"""


def rotate90(matrix):
    n = len(matrix)
    return [[matrix[n - j - 1][i] for j in range(n)] for i in range(n)]


def rotate180(matrix):
    return rotate90(rotate90(matrix))


def rotate270(matrix):
    return rotate90(rotate90(rotate90(matrix)))


def reflect(matrix):
    return [row[::-1] for row in matrix]


# Read input
with open("transform.in", "r") as fin:
    lines = [line.strip() for line in fin.readlines()]
n = int(lines[0])
original = [list(lines[i]) for i in range(1, n + 1)]
target = [list(lines[i]) for i in range(n + 1, 2 * n + 1)]

result = 7  # Default to invalid transformation

# Check each transformation in order
# Check 90 rotation
if rotate90(original) == target:
    result = 1
elif rotate180(original) == target:
    result = 2
elif rotate270(original) == target:
    result = 3
elif reflect(original) == target:
    result = 4
else:
    # Check combination (reflection + rotation)
    reflected = reflect(original)
    if (
        rotate90(reflected) == target
        or rotate180(reflected) == target
        or rotate270(reflected) == target
    ):
        result = 5
    elif original == target:
        result = 6

# Write the result to the output file
with open("transform.out", "w") as fout:
    fout.write(f"{result}\n")
