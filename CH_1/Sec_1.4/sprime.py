"""
ID: amolgur1
LANG: PYTHON3
TASK: sprime
"""

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def dfs(val, length):
    if length == N:
        results.append(val)
        return
    for d in (1, 3, 7, 9):
        nxt = val * 10 + d
        if is_prime(nxt):
            dfs(nxt, length + 1)

with open('sprime.in', 'r') as fin:
    N = int(fin.readline().strip())

results = []

if N == 1:
    results = [2, 3, 5, 7]
else:
    for seed in (2, 3, 5, 7):
        dfs(seed, 1)

results.sort()

with open('sprime.out', 'w') as fout:
    for num in results:
        fout.write(f"{num}\n")