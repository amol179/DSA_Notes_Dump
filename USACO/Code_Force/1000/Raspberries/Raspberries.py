def solve():
    import sys

    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    pos = 1
    out_lines = []

    # Function to count factors of 2 in x
    def v2(x):
        cnt = 0
        while x % 2 == 0:
            cnt += 1
            x //= 2
        return cnt

    for _ in range(t):
        n = int(input_data[pos])
        pos += 1
        k = int(input_data[pos])
        pos += 1
        a = list(map(int, input_data[pos : pos + n]))
        pos += n

        if k in (2, 3, 5):
            # For prime k, if any element is divisible by k, product is divisible by k.
            if any(x % k == 0 for x in a):
                out_lines.append("0")
            else:
                best = float("inf")
                # For each number, the cost is the increment required
                # to make it divisible by k:
                for x in a:
                    rem = x % k
                    cost = (
                        k - rem
                    ) % k  # When rem==0, cost would be 0 but that case is handled above.
                    best = min(best, cost)
                out_lines.append(str(best))
        elif k == 4:
            # k=4 means the product must have at least 2 factors of 2.
            total2 = sum(v2(x) for x in a)
            if total2 >= 2:
                out_lines.append("0")
                continue
            deficit = 2 - total2  # Either 1 or 2 factors needed.
            INF = 10**9
            best1_list = []  # cost to get at least +1 factor (gain>=1)
            best2_list = []  # cost to get at least +2 factors (gain>=2)
            # For each element, try a small number of increments
            for x in a:
                base = v2(x)
                cost1 = INF
                cost2 = INF
                # The range here is safe because a[i] is small (<=10)
                for op in range(51):
                    new_val = x + op
                    new2 = v2(new_val)
                    gain = new2 - base
                    if gain >= 1:
                        cost1 = min(cost1, op)
                    if gain >= 2:
                        cost2 = min(cost2, op)
                best1_list.append(cost1)
                best2_list.append(cost2)

            ans = INF
            if deficit == 1:
                ans = min(best1_list)
            elif deficit == 2:
                # Option A: a single element upgraded to gain at least 2 extra factors.
                for c in best2_list:
                    ans = min(ans, c)
                # Option B: upgrade two different elements for +1 factor each.
                sorted_costs = sorted(best1_list)
                if len(sorted_costs) >= 2:
                    ans = min(ans, sorted_costs[0] + sorted_costs[1])
            out_lines.append(str(ans))
    sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    solve()
