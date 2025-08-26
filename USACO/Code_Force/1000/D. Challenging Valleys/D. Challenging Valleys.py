def is_valley(arr):
    n = len(arr)
    l = r = -1

    # Find the largest subarray of equal elements
    i = 0
    while i < n:
        start = i
        while i + 1 < n and arr[i] == arr[i + 1]:
            i += 1
        end = i

        # Check the surrounding conditions
        if (start == 0 or arr[start - 1] > arr[start]) and (
            end == n - 1 or arr[end] < arr[end + 1]
        ):
            if l == -1:  # First occurrence
                l, r = start, end
            else:  # More than one valid subarray
                return "NO"
        i += 1

    # Ensure exactly one valid subarray
    return "YES" if l != -1 else "NO"


# Read input
t = int(input())
results = []

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    results.append(is_valley(arr))

# Output results
print("\n".join(results))
