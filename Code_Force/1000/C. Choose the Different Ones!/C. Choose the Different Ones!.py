def solve():
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))

        # Create sets of the numbers in [1, k] from both arrays
        set_a = {x for x in a if 1 <= x <= k}
        set_b = {x for x in b if 1 <= x <= k}

        # Check that the union covers all required numbers from 1 to k.
        if set_a | set_b != set(range(1, k + 1)):
            print("NO")
            continue

        # Determine numbers that appear only in one array
        A_only = set_a - set_b
        B_only = set_b - set_a

        # Since we must choose exactly k/2 from each array:
        # The forced numbers from a (A_only) and from b (B_only) must not exceed k/2 each.
        if len(A_only) > k // 2 or len(B_only) > k // 2:
            print("NO")
        else:
            print("YES")


if __name__ == "__main__":
    solve()
