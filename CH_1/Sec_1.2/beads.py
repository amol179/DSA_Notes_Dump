"""
ID: amolgur1
LANG: PYTHON3
TASK: beads
"""

with open("beads.in", "r") as f:
    n = int(f.readline().strip())
    s = f.readline().strip()
s += s

max_total = 0

for i in range(n):
    window = s[i : i + n]
    left_r = 0
    for bead in window:
        if bead == "r" or bead == "w":
            left_r += 1
        else:
            break

    left_b = 0
    for bead in window:
        if bead == "b" or bead == "w":
            left_b += 1
        else:
            break

    right_r = 0
    for bead in reversed(window):
        if bead == "r" or bead == "w":
            right_r += 1
        else:
            break

    right_b = 0
    for bead in reversed(window):
        if bead == "b" or bead == "w":
            right_b += 1
        else:
            break

    left_max = max(left_r, left_b)
    right_max = max(right_r, right_b)
    total = left_max + right_max

    # Ensure total does not exceed n
    if total > n:
        total = n

    if total > max_total:
        max_total = total


with open("beads.out", "w") as fout:
    fout.write(f"{max_total}\n")
