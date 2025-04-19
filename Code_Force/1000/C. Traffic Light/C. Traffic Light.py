def min_wait_time(n, c, s):
    max_wait = 0
    green_positions = [i for i in range(n) if s[i] == "g"]

    for i in range(n):
        if s[i] == c:
            # Find the next green light safely
            next_green = min((pos for pos in green_positions if pos >= i), default=n)
            wait_time = next_green - i
            max_wait = max(max_wait, wait_time)

    return max_wait


# Read input without sys
t = int(input().strip())
results = []

for _ in range(t):
    n, c = input().split()
    n = int(n)
    s = input().strip()
    results.append(str(min_wait_time(n, c, s)))

print("\n".join(results))
