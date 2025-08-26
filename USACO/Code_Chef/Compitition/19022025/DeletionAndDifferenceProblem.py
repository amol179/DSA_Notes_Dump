def solve():
    import sys
    from collections import Counter

    data = sys.stdin.read().strip().split()
    if not data:
        return
    t = int(data[0])
    index = 1
    results = []

    for _ in range(t):
        n = int(data[index])
        index += 1
        arr = list(map(int, data[index : index + n]))
        index += n

        # Count frequency of each number
        freq = Counter(arr)
        # Count leftover nonzero numbers after pairing (they occur with odd frequency)
        leftover_nonzero = sum(1 for x, f in freq.items() if x != 0 and f % 2 == 1)

        # Determine if we have a 0:
        # Either originally present or produced from pairing any number (nonzero element with frequency >= 2)
        has_zero = freq.get(0, 0) > 0 or any(f >= 2 for x, f in freq.items() if x != 0)

        # Final length is the number of leftover nonzero elements plus 1 zero if exists.
        final_length = leftover_nonzero + (1 if has_zero else 0)
        results.append(str(final_length))

    sys.stdout.write("\n".join(results))


if __name__ == "__main__":
    solve()
