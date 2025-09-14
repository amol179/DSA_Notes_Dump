"""
ID: amolgur1
LANG: PYTHON3
TASK: theme
"""

def read_input():
    """Reads input from theme.in."""
    with open("theme.in", "r") as fin:
        N = int(fin.readline())
        notes = []
        while len(notes) < N:
            notes.extend(map(int, fin.readline().strip().split()))
    return N, notes

def write_output(ans):
    """Writes the final answer to theme.out."""
    with open("theme.out", "w") as fout:
        fout.write(str(ans) + "\n")

def check(L, intervals):
    """
    Checks if a non-overlapping, repeated interval sequence of length L exists.
    Uses rolling hash with verification to avoid collisions.
    """
    if L < 4:  # A theme must have at least 5 notes, so the interval sequence must have length >= 4.
        return False

    base = 257
    mod = 10**9 + 7
    n = len(intervals)
    
    # Map intervals from [-87, 87] to a non-negative range for safer hashing.
    mapped_intervals = [val + 87 for val in intervals]

    # Calculate the hash of the first substring of length L
    hash_val = 0
    power = 1
    for i in range(L):
        hash_val = (hash_val * base + mapped_intervals[i]) % mod
        if i < L - 1:
            power = (power * base) % mod

    # 'seen' stores the first index where a hash value was encountered.
    seen = {hash_val: 0}
    
    # Slide the window across the rest of the interval array
    for i in range(1, n - L + 1):
        # Update hash value using the rolling hash technique
        hash_val = (hash_val - mapped_intervals[i - 1] * power) % mod
        hash_val = (hash_val * base + mapped_intervals[i + L - 1]) % mod
        
        # Ensure the hash value remains positive
        if hash_val < 0:
            hash_val += mod

        if hash_val in seen:
            j = seen[hash_val]
            # Check for non-overlapping condition. A theme of length (L+1)
            # requires the start of the second theme to be at least (L+1)
            # positions after the start of the first.
            if i - j >= L + 1:
                # IMPORTANT: Verify the match to prevent false positives from hash collisions.
                if intervals[i:i+L] == intervals[j:j+L]:
                    return True # Verified match found.
        
        # If we haven't seen this hash before, record its first position.
        if hash_val not in seen:
            seen[hash_val] = i
            
    return False

def main():
    """Main logic to find the longest theme."""
    N, notes = read_input()
    
    # A theme requires at least 5 notes, and two non-overlapping themes
    # require at least 10 notes in total.
    if N < 10:
        write_output(0)
        return

    intervals = [notes[i+1] - notes[i] for i in range(N - 1)]
    
    # Binary search for the theme length (mid).
    # The maximum possible theme length is N // 2.
    low, high = 5, N // 2
    ans = 0
    
    while low <= high:
        mid = (low + high) // 2
        if mid == 0: # Avoid checking for length 0
            break
        # Check for an interval sequence of length mid - 1
        if check(mid - 1, intervals):
            ans = mid      # This length is possible, try for a longer one.
            low = mid + 1
        else:
            high = mid - 1 # This length is not possible, try a shorter one.
            
    write_output(ans)

if __name__ == "__main__":
    main()