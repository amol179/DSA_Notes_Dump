def solve():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    index = 1
    out_lines = []
    for _ in range(t):
        n = int(data[index])
        index += 1
        arr = list(map(int, data[index:index+n]))
        index += n
        
        # If n < 2, then any chosen subsequence would make the complement empty.
        if n < 2:
            out_lines.append("-1")
            continue
        
        freq = {}
        candidate = None
        for x in arr:
            freq[x] = freq.get(x, 0) + 1
        # Look for an element that appears at least twice.
        for x in arr:
            if freq[x] >= 2:
                candidate = x
                break
        
        if candidate is None:
            out_lines.append("-1")
        else:
            # We output a cool subsequence of length 1: [candidate].
            # For B = [candidate], its only non-empty subsequence is [candidate] whose average is candidate.
            # Since candidate appears at least twice in A, it is present in the complement.
            out_lines.append("1")
            out_lines.append(str(candidate))
    
    sys.stdout.write("\n".join(out_lines))

if __name__ == '__main__':
    solve()
