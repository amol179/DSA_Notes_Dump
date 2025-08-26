def can_make_zero(n, a):
    for i in range(n - 2):
        if a[i] < 0:  # If any number goes negative, it's impossible
            return "NO"

        # Apply operation: reduce a[i], modify a[i+1] and a[i+2]
        diff = a[i]  # The amount to nullify at this index
        a[i] -= diff
        a[i + 1] -= 2 * diff
        a[i + 2] -= diff

    return "YES" if all(x == 0 for x in a) else "NO"


# Read input
t = int(input())  # Number of test cases

for _ in range(t):
    n = int(input())  # Number of elements
    a = list(map(int, input().split()))  # Array elements
    print(can_make_zero(n, a))
