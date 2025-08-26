"""
ID: amolgur1
LANG: PYTHON3
TASK: milk2
"""

with open("milk2.in", "r") as fin:
    n = int(fin.readline())
    intervals = []
    for _ in range(n):
        s, e = map(int, fin.readline().split())
        intervals.append((s, e))

intervals.sort()

merged = []

for interval in intervals:
    if not merged:
        merged.append(interval)
    else:
        last_s, last_e = merged[-1]
        current_s, current_e = interval

        if current_s <= last_e:
            new_e = max(last_e, current_e)
            merged[-1] = (last_s, new_e)
        else:
            merged.append((current_s, current_e))

max_milking = 0
for s, e in merged:
    max_milking = max(max_milking, e - s)

max_idle = 0
for i in range(1, len(merged)):
    gap = merged[i][0] - merged[i - 1][1]
    if gap > max_idle:
        max_idle = gap

with open("milk2.out", "w") as fout:
    fout.write(f"{max_milking} {max_idle}\n")
