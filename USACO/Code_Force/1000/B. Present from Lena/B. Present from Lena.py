def print_handkerchief(n):
    # Upper half (including the middle row)
    for i in range(n + 1):
        # Leading spaces
        line = "  " * (n - i)
        # Increasing numbers
        line += " ".join(str(j) for j in range(i + 1))
        # Decreasing numbers
        if i > 0:
            line += " " + " ".join(str(j) for j in range(i - 1, -1, -1))
        print(line.rstrip())  # Ensure no trailing spaces

    # Lower half
    for i in range(n - 1, -1, -1):
        # Leading spaces
        line = "  " * (n - i)
        # Increasing numbers
        line += " ".join(str(j) for j in range(i + 1))
        # Decreasing numbers
        if i > 0:
            line += " " + " ".join(str(j) for j in range(i - 1, -1, -1))
        print(line.rstrip())  # Ensure no trailing spaces


# Input n
n = int(input())
print_handkerchief(n)
