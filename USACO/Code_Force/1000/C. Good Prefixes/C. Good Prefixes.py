def solve():
    import sys

    # sys

    data = sys.stdin.read().strip().split()
    t = int(data[0])
    idx = 1

    out = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1

        prefix_sum = 0
        # Python ints are unbounded, but we mimic "LLONG_MIN" with a large negative:
        max_val = -(10**15)
        count_occurrences = 0

        for __ in range(n):
            x = int(data[idx])
            idx += 1

            prefix_sum += x
            if x > max_val:
                max_val = x

            if prefix_sum == 2 * max_val:
                count_occurrences += 1

        out.append(str(count_occurrences))

    print("\n".join(out))
