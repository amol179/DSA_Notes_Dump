def solve():
    import sys, bisect
    data = sys.stdin.read().splitlines()
    if not data:
        return
    t = int(data[0].strip())
    out_lines = []
    line_index = 1
    for _ in range(t):
        if line_index >= len(data):
            break
        A = data[line_index].strip()
        line_index += 1
        if line_index >= len(data):
            break
        B = data[line_index].strip()
        line_index += 1
        
        n = len(A)
        m = len(B)
        
        # Build a dictionary for positions (1-indexed) for each character in A.
        pos_dict = {}
        for i, ch in enumerate(A, start=1):
            if ch not in pos_dict:
                pos_dict[ch] = []
            pos_dict[ch].append(i)
        
        # Greedily choose positions for B (from right to left) to maximize the kept index sum.
        current_bound = n + 1  # We need positions strictly less than current_bound.
        kept_sum = 0
        possible = True
        
        # Process B from its last character to the first.
        for ch in reversed(B):
            if ch not in pos_dict:
                possible = False
                break
            lst = pos_dict[ch]
            # Use binary search: find the insertion point for current_bound.
            idx = bisect.bisect_left(lst, current_bound)
            if idx == 0:
                possible = False
                break
            chosen = lst[idx - 1]
            kept_sum += chosen
            current_bound = chosen  # Next chosen must be before this index.
        
        if not possible:
            out_lines.append("-1")
        else:
            total = n * (n + 1) // 2
            removals = n - m
            penalty = removals * (removals - 1) // 2
            cost = total - kept_sum - penalty
            out_lines.append(str(cost))
    
    sys.stdout.write("\n".join(out_lines))

if __name__ == '__main__':
    solve()
