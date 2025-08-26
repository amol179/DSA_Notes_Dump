"""
ID: amolgur1
LANG: PYTHON3
TASK: barn1
"""

with open("barn1.in", "r") as f:
    M, S, C = map(int, f.readline().split())
    stalls = [int(f.readline().strip()) for _ in range(C)]

result = 0
if C == 0:
    result = 0
else:
    stalls.sort()
    first = stalls[0]
    last = stalls[-1]
    initial_length = last - first + 1

    gaps = []
    for i in range(1, len(stalls)):
        gap = stalls[i] - stalls[i - 1] - 1
        if gap > 0:
            gaps.append(gap)

    gaps.sort(reverse=True)
    sum_gaps = sum(gaps[: M - 1])  # Take up to M-1 largest gaps

    result = initial_length - sum_gaps

with open("barn1.out", "w") as f:
    f.write(f"{result}\n")
