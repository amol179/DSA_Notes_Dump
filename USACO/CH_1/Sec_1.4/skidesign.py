"""
ID: amolgur1
LANG: PYTHON3
TASK: skidesign
"""

with open("skidesign.in", "r") as fin:
    lines = fin.readlines()

N = int(lines[0].strip())
heights = [int(line.strip()) for line in lines[1:]]

heights.sort()

min_cost = float("inf")

# 84 - 100 = 16 not allowed so only till 83
for low in range(0, 84):
    high = low + 17
    current_cost = 0

    for h in heights:
        if h < low:
            current_cost += (low - h) ** 2
        elif h > high:
            current_cost += (h - high) ** 2

    min_cost = min(min_cost, current_cost)

with open("skidesign.out", "w") as fout:
    fout.write(str(min_cost) + "\n")
