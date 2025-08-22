"""
ID: amolgur1
LANG: PYTHON3
TASK: fact4
"""


def rightmost_nonzero_digit(n):
    result = 1
    count_2 = 0
    count_5 = 0

    for i in range(2, n + 1):
        x = i

        # Remove factors of 2 and 5
        while x % 2 == 0:
            x //= 2
            count_2 += 1
        while x % 5 == 0:
            x //= 5
            count_5 += 1

        # Multiply remaining part modulo 10
        result = (result * x) % 10

    # Restore leftover 2s that didn’t pair with 5s
    for _ in range(count_2 - count_5):
        result = (result * 2) % 10

    return result

# Read input from file
with open("fact4.in", "r") as infile:
    n = int(infile.readline().strip())

# Compute result
digit = rightmost_nonzero_digit(n)

# Write output to file
with open("fact4.out", "w") as outfile:
    outfile.write(str(digit) + "\n")