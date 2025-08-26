"""
ID: amolgur1
LANG: PYTHON3
TASK: combo
"""


def valid_positions(target, N):

    vals = set()
    for offset in range(-2, 3):
        adjusted = ((target - 1 + offset) % N) + 1
        vals.add(adjusted)
    return vals


with open("combo.in", "r") as fin:
    N = int(fin.readline().strip())
    combo1 = list(map(int, fin.readline().strip().split()))
    combo2 = list(map(int, fin.readline().strip().split()))

valid_fj = [valid_positions(combo1[i], N) for i in range(3)]
valid_master = [valid_positions(combo2[i], N) for i in range(3)]

valid_set = set()

for a in valid_fj[0]:
    for b in valid_fj[1]:
        for c in valid_fj[2]:
            valid_set.add((a, b, c))


for a in valid_master[0]:
    for b in valid_master[1]:
        for c in valid_master[2]:
            valid_set.add((a, b, c))

with open("combo.out", "w") as fout:
    fout.write(f"{len(valid_set)}\n")
