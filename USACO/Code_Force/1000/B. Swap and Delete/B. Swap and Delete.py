def min_cost_to_make_good(s: str) -> int:
    n = len(s)
    totalZeros = s.count("0")
    totalOnes = s.count("1")

    prefixZeros = 0
    prefixOnes = 0
    max_L = 0

    for i in range(n):
        if s[i] == "0":
            prefixZeros += 1
        else:
            prefixOnes += 1
        # Check if the current prefix of length (i+1) satisfies the conditions
        if prefixZeros <= totalOnes and prefixOnes <= totalZeros:
            max_L = i + 1
        else:
            break  # further increasing L will only add more counts

    return n - max_L


# Processing multiple test cases
t = int(input().strip())
for _ in range(t):
    s = input().strip()
    print(min_cost_to_make_good(s))
