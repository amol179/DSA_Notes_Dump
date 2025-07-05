"""
ID: amolgur1
LANG: PYTHON3
TASK: frac1
"""

# 2 3 attempts , 10th tc me issue hua tha


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def compare(frac1, frac2):
    a, b = frac1
    c, d = frac2
    return a * d - c * b  # negative if frac1 < frac2

def merge_sort(fractions):
    if len(fractions) <= 1:
        return fractions
    mid = len(fractions) // 2
    left = merge_sort(fractions[:mid])
    right = merge_sort(fractions[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]) <= 0:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def generate_fractions(N):
    fractions = []
    for d in range(1, N + 1):
        for n in range(0, d + 1):
            if gcd(n, d) == 1:
                fractions.append((n, d))
    return merge_sort(fractions)

# File I/O
with open('frac1.in', 'r') as f:
    N = int(f.readline().strip())

fractions = generate_fractions(N)

with open('frac1.out', 'w') as out:
    for n, d in fractions:
        out.write(f"{n}/{d}\n")