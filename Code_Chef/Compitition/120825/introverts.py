import sys

def is_valid_permutation(N, P):
    # Build an array pos so that pos[x] is the seat (1-indexed) where person x sits.
    pos = [0]*(N+1)
    for i, person in enumerate(P):
        pos[person] = i + 1
    # Person 1 must be at an endpoint.
    if pos[1] != 1 and pos[1] != N:
        return False

    # Initial free interval:
    # If Person 1 sits at seat 1 then the free seats are 2..N, represented by (1, N+1).
    # Otherwise (Person 1 sits at N) the free seats are 1..N-1, represented by (0, N).
    if pos[1] == 1:
        init_interval = (1, N + 1)
    else:
        init_interval = (0, N)

    # Inline functions for potential and allowed candidate(s).
    # We use bit‐shifts for integer division by 2.
    def get_pot(l, r):
        if l == 0:
            return r - 1
        elif r == N + 1:
            return N - l
        else:
            return (r - l) >> 1  # equivalent to (r-l)//2

    def get_allowed(l, r):
        if l == 0:
            return (1,)
        elif r == N + 1:
            return (N,)
        else:
            gap = r - l - 1
            if gap & 1:  # odd gap
                return (l + ((gap + 1) >> 1),)
            else:
                mid = l + (gap >> 1)
                return (mid, mid + 1)

    # Create buckets: an array (index 0..N) of dictionaries.
    # For each interval with potential p, for each allowed candidate s,
    # we store buckets[p][s] = (l, r).
    buckets = [dict() for _ in range(N + 1)]
    init_pot = get_pot(init_interval[0], init_interval[1])
    for cand in get_allowed(init_interval[0], init_interval[1]):
        buckets[init_pot][cand] = init_interval
    max_pot = init_pot

    # Process persons 2 through N in increasing order.
    for person in range(2, N + 1):
        s = pos[person]
        # Adjust max_pot downward if needed.
        while max_pot >= 0 and not buckets[max_pot]:
            max_pot -= 1
        if max_pot < 0:
            return False  # no active interval remains
        # The chosen seat must be an allowed candidate from an interval with maximum potential.
        if s not in buckets[max_pot]:
            return False
        # Retrieve and remove the interval from which s is chosen.
        interval = buckets[max_pot].pop(s)
        l, r = interval
        # If the interval has two allowed candidates, remove the other candidate as well.
        for cand in get_allowed(l, r):
            if cand != s:
                if cand in buckets[max_pot] and buckets[max_pot][cand] == interval:
                    del buckets[max_pot][cand]
        # Split the interval at seat s into up to two new intervals.
        if s - l - 1 > 0:
            new_interval = (l, s)
            new_pot = get_pot(new_interval[0], new_interval[1])
            for cand in get_allowed(new_interval[0], new_interval[1]):
                buckets[new_pot][cand] = new_interval
            if new_pot > max_pot:
                max_pot = new_pot
        if r - s - 1 > 0:
            new_interval = (s, r)
            new_pot = get_pot(new_interval[0], new_interval[1])
            for cand in get_allowed(new_interval[0], new_interval[1]):
                buckets[new_pot][cand] = new_interval
            if new_pot > max_pot:
                max_pot = new_pot
    return True

    
def main():
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    index = 1
    output_lines = []
    for _ in range(t):
        N = int(data[index])
        index += 1
        P = list(map(int, data[index:index + N]))
        index += N
        output_lines.append("YES" if is_valid_permutation(N, P) else "NO")
    sys.stdout.write("\n".join(output_lines))
    
if __name__ == "__main__":
    main()
