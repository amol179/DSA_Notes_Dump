def solve():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    out_lines = []
    # We define each node as a tuple:
    # (parity, f0_0, f0_1, f1_0, f1_1)
    # where:
    #   parity = 1 if segment length is odd, 0 if even.
    #   f0 = (f0_0, f0_1) : function if starting operator is "&"
    #   f1 = (f1_0, f1_1) : function if starting operator is "|"
    # and the beauty of a segment is f0(1) = f0_1.
    
    def merge_nodes(L, R):
        # Unpack L and R:
        pL, l0, l1, l_f0, l_f1 = L  # L.f0 = (l0, l1) and L.f1 = (l_f0, l_f1)
        pR, r0, r1, r_f0, r_f1 = R
        # Determine the operator for R based on L’s parity:
        # If L is odd then the next operator is "&" (represented as 0)
        # otherwise it is "|" (represented as 1).
        if pL == 1:
            F = (r0, r1)   # use R.f0: (r0, r1)
        else:
            F = (r_f0, r_f1)  # use R.f1: (r_f0, r_f1)
        # Now, for each starting operator op in {0,1} we define:
        #   merged.f[op](x) = R.f[?]( L.f[op](x) )
        new_f0_0 = F[l0]      # for op = 0 and input 0
        new_f0_1 = F[l1]      # for op = 0 and input 1
        new_f1_0 = F[l_f0]    # for op = 1 and input 0
        new_f1_1 = F[l_f1]    # for op = 1 and input 1
        new_parity = (pL + pR) & 1
        return (new_parity, new_f0_0, new_f0_1, new_f1_0, new_f1_1)
    
    # Process test cases:
    for _ in range(t):
        n = int(data[idx]); idx += 1
        arr = list(map(int, data[idx: idx+n])); idx += n
        q = int(data[idx]); idx += 1
        
        # Build iterative segment tree.
        size = 1
        while size < n:
            size *= 2
        tree = [None] * (2*size)
        # Initialize leaves:
        for i in range(size):
            if i < n:
                a = arr[i]
                # leaf: parity = 1; f0 = (0, a) and f1 = (a, 1)
                tree[size+i] = (1, 0, a, a, 1)
            else:
                # For “dummy” leaves we want an identity transformation.
                # Think of an empty segment: length 0 (even) and f(x)= x.
                tree[size+i] = (0, 0, 1, 0, 1)
        # Build internal nodes:
        for i in range(size-1, 0, -1):
            tree[i] = merge_nodes(tree[2*i], tree[2*i+1])
        
        # The overall beauty is tree[1]'s f0(1) i.e. tree[1][2].
        # Process queries:
        for _q in range(q):
            pos = int(data[idx]); 
            new_val = int(data[idx+1]); 
            idx += 2
            pos -= 1  # convert to 0-index
            leaf_index = size + pos
            tree[leaf_index] = (1, 0, new_val, new_val, 1)
            i_node = leaf_index // 2
            while i_node:
                tree[i_node] = merge_nodes(tree[2*i_node], tree[2*i_node+1])
                i_node //= 2
            out_lines.append(str(tree[1][2]))
    sys.stdout.write("\n".join(out_lines))

if __name__ == '__main__':
    solve()
