import sys
import bisect

def is_valid_permutation(N, P):
    """
    Given an integer N and a permutation P of [1..N] representing the final seating
    arrangement (where the i-th number in P is the person sitting in seat i, seats numbered 1..N),
    this function simulates a “greedy” seating process:
    
      - Person 1 must sit at an endpoint (seat 1 or seat N).
      - For persons 2 through N (in increasing order), when they arrive they choose a seat 
        from among the currently available seats that maximizes the distance to the nearest occupied seat.
      - If more than one seat is optimal (i.e. gives the same maximum distance), either choice is allowed.
    
    The available seats are maintained as disjoint intervals. Each interval is stored as a tuple (l, r)
    meaning that the free seats are l+1, l+2, …, r-1. (Here l or r may be “artificial” boundaries:
    0 or N+1.)
    
    In an interval:
      - If it touches the left end (l == 0), the only optimal seat is l+1.
      - If it touches the right end (r == N+1), the only optimal seat is r-1.
      - Otherwise (both boundaries are occupied), if the number of free seats is odd the unique
        optimal seat is the middle seat, and if even, the two central seats are both allowed.
    
    The function returns True if the seating order (determined by the positions of person 1, 2, …, N)
    is consistent with such a process; otherwise it returns False.
    """
    # Build a mapping: pos[x] is the seat (1-indexed) where person x sits.
    pos = [0] * (N + 1)
    for i, person in enumerate(P):
        pos[person] = i + 1

    # Person 1 must sit at an endpoint.
    if pos[1] not in (1, N):
        return False

    # intervals is a list of available intervals sorted by the left boundary.
    # An interval (l, r) represents free seats: l+1, l+2, ..., r-1.
    intervals = []
    if pos[1] == 1:
        # Person 1 sits at the left end.
        # The only available seats are 2 through N, so we set boundaries as (1, N+1)
        # (1 is occupied and N+1 is an artificial boundary).
        intervals.append((1, N + 1))
    else:
        # Person 1 sits at the right end.
        intervals.append((0, N))  # (0 is artificial, N is occupied)

    # Helper: insert an interval if it contains any free seats.
    def insert_interval(interval):
        l, r = interval
        if r - l - 1 > 0:
            bisect.insort(intervals, interval)

    # Process persons 2 through N (in increasing order).
    for person in range(2, N + 1):
        s = pos[person]
        # Locate the interval that contains seat s.
        # Since intervals are sorted by left boundary, we use bisect.
        i = bisect.bisect_right(intervals, (s, float('inf'))) - 1
        if i < 0:
            return False
        l, r = intervals[i]
        if not (l < s < r):
            return False

        # Determine the allowed (optimal) candidate seat(s) for interval (l, r).
        if l == 0:
            # Interval touches the left end: the only allowed seat is l+1.
            allowed = {l + 1}
        elif r == N + 1:
            # Interval touches the right end: the only allowed seat is r-1.
            allowed = {r - 1}
        else:
            # Both boundaries are actual occupied seats.
            available = r - l - 1  # number of free seats in (l, r)
            if available % 2 == 1:
                # A unique middle seat.
                candidate = l + (available + 1) // 2
                allowed = {candidate}
            else:
                # Two optimal choices (both central seats yield the same minimum distance).
                candidate1 = l + available // 2
                candidate2 = candidate1 + 1
                allowed = {candidate1, candidate2}

        if s not in allowed:
            return False

        # Remove the interval (l, r) and add back the two new intervals after seating at s.
        intervals.pop(i)
        insert_interval((l, s))
        insert_interval((s, r))
        
    return True

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        N = int(data[index])
        index += 1
        P = list(map(int, data[index:index + N]))
        index += N
        results.append("YES" if is_valid_permutation(N, P) else "NO")
    print("\n".join(results))

if __name__ == "__main__":
    main()
