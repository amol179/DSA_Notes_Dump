"""
ID: amolgur1
LANG: PYTHON3
TASK: milk
"""

with open("milk.in", "r") as fin:
    data = fin.read().split()
    idx = 0
    N = int(data[idx])
    idx += 1
    M = int(data[idx])
    idx += 1
    farmers = []
    for _ in range(M):
        Pi = int(data[idx])
        Ai = int(data[idx + 1])
        farmers.append((Pi, Ai))
        idx += 2

total = 0
if N > 0:
    farmers.sort()
    remaining = N
    for price, amount in farmers:
        if remaining <= 0:
            break
        take = min(remaining, amount)
        total += take * price
        remaining -= take

with open("milk.out", "w") as fout:
    fout.write(f"{total}\n")
