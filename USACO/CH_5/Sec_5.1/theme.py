"""
ID: amolgur1
LANG: PYTHON3
TASK: theme
"""

def read_input():
    fin = open("theme.in", "r")
    N = int(fin.readline())
    notes = []
    while len(notes) < N:
        notes.extend(map(int, fin.readline().strip().split()))
    fin.close()
    return N, notes

def write_output(ans):
    fout = open("theme.out", "w")
    fout.write(str(ans) + "\n")
    fout.close()

def check(L, intervals):
    base = 257
    mod = 10**9 + 7
    n = len(intervals)
    hash_val = 0
    power = 1
    for i in range(L):
        hash_val = (hash_val * base + intervals[i]) % mod
        if i < L - 1:
            power = (power * base) % mod

    seen = {hash_val: 0}
    for i in range(1, n - L + 1):
        hash_val = (hash_val - intervals[i - 1] * power) % mod
        hash_val = (hash_val * base + intervals[i + L - 1]) % mod
        if hash_val in seen and abs(seen[hash_val] - i) >= L + 1:
            return True
        if hash_val not in seen:
            seen[hash_val] = i
    return False

def main():
    N, notes = read_input()
    if N < 5:
        write_output(0)
        return

    intervals = [notes[i+1] - notes[i] for i in range(N - 1)]
    low, high = 5, N
    ans = 0
    while low <= high:
        mid = (low + high) // 2
        if check(mid - 1, intervals):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    write_output(ans)

main()