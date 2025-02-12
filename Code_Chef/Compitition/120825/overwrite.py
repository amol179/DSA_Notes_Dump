def solve():
    import sys,sys,sys
    data = sys.stdin.buffer.read().split()
    if not data: 
        return
    t = int(data[0])
    index = 1
    out_lines = []
    # We know that the maximum length of A (and m) is at most 2e5;
    # we precompute a power–table for rolling–hashes up to, say, 210000.
    MAX_POW = 210000
    mod = 10**9+7
    base = 137
    pow_arr = [1]*(MAX_POW)
    for i in range(1, MAX_POW):
        pow_arr[i] = (pow_arr[i-1] * base) % mod

    # --- Rolling hash functions. ---
    def build_hash(arr):
        n = len(arr)
        H = [0]*(n+1)
        for i in range(n):
            H[i+1] = (H[i]*base + arr[i]) % mod
        return H

    def query_hash(H, l, r):
        return (H[r] - H[l] * pow_arr[r-l]) % mod

    # --- Binary search for LCP length between A[x_start:x_start+L] and Y[0:L] ---
    def lcp_length(Hx, x_start, Hy, L_val):
        lo = 0
        hi = L_val+1
        while lo < hi:
            mid = (lo + hi) >> 1
            if mid > L_val:
                hi = mid
                continue
            if query_hash(Hx, x_start, x_start+mid) == query_hash(Hy, 0, mid):
                lo = mid + 1
            else:
                hi = mid
        return lo - 1

    # --- Compare A[i:i+m] with L ---
    def compare_segment_A(i, m, hashA, A_arr, hashL, L_arr):
        lcp = lcp_length(hashA, i, hashL, m)
        if lcp >= m:
            return 0
        a = A_arr[i+lcp]
        b = L_arr[lcp]
        if a > b:
            return 1
        elif a < b:
            return -1
        return 0

    # --- Booth algorithm: return lexicographically smallest cyclic rotation of arr ---
    def booth(arr):
        n = len(arr)
        i = 0
        j = 1
        k = 0
        while i < n and j < n and k < n:
            ai = arr[(i+k) % n]
            aj = arr[(j+k) % n]
            if ai == aj:
                k += 1
                continue
            if ai > aj:
                i = i + k + 1
                if i <= j:
                    i = j + 1
            else:
                j = j + k + 1
                if j <= i:
                    j = i + 1
            k = 0
        start = min(i, j)
        return arr[start:] + arr[:start]

    # --- Process each test case ---
    import bisect
    for _ in range(t):
        if index >= len(data): break
        n = int(data[index]); index += 1
        m = int(data[index]); index += 1
        A = [int(x) for x in data[index:index+n]]
        index += n
        B = [int(x) for x in data[index:index+m]]
        index += m

        # (m<=n always)
        if m > 0:
            L = booth(B)
        else:
            L = []
        # Precompute hash for A and for L.
        hashA = build_hash(A)
        hashL = build_hash(L)
        # Valid op–start positions are i=1,...,K where K=n-m+1.
        K = n - m + 1

        # --- Decide the op–positions.
        # We “simulate” a decision rule: if no op covers i then compare A[i..i+m-1] with L.
        # (Indices here are 1–based; note that A is 0–indexed.)
        S = []  # will store op–start positions (1–based)
        for i in range(1, K+1):
            if not S or i >= S[-1] + m:
                cmp_val = compare_segment_A(i-1, m, hashA, A, hashL, L)
                if cmp_val > 0:
                    S.append(i)
            else:
                # if i is inside the coverage of the last op, then since L[0] is the smallest letter,
                # it is always beneficial to “reset” (i.e. start a new op) so we add i.
                S.append(i)

        # --- Construct final answer F.
        # For each j=1,...,n (1–based), let s be the last op in S with s<=j.
        # If such s exists and j <= s+m–1 then F[j] = L[j–s] (with 0–based index for L).
        # Otherwise F[j] = A[j].
        F = [0]*n
        for j in range(1, n+1):
            pos = bisect.bisect_right(S, j) - 1
            if pos >= 0:
                s_val = S[pos]
                if j <= s_val + m - 1:
                    F[j-1] = L[j - s_val]
                else:
                    F[j-1] = A[j-1]
            else:
                F[j-1] = A[j-1]
        out_lines.append(" ".join(str(x) for x in F))
    sys.stdout.write("\n".join(out_lines))

if __name__ == '__main__':
    solve()
