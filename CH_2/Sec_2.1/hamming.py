"""
ID: amolgur1
LANG: PYTHON3
TASK: hamming
"""

def hamming_distance(a, b):
    xor = a ^ b
    count = 0
    while xor:
        count += xor & 1
        xor >>= 1
    return count

def is_valid(candidate, selected, D):
    for code in selected:
        if hamming_distance(candidate, code) < D:
            return False
    return True

def generate_codewords(N, B, D):
    max_code = 1 << B
    selected = []
    for i in range(max_code):
        if is_valid(i, selected, D):
            selected.append(i)
            if len(selected) == N:
                break
    return selected


with open("hamming.in", "r") as f:
    N, B, D = map(int, f.readline().strip().split())

result = generate_codewords(N, B, D)

with open("hamming.out", "w") as f:
    for i in range(len(result)):
        f.write(str(result[i]))
        if (i + 1) % 10 == 0 or i == len(result) - 1:
            f.write("\n")
        else:
            f.write(" ")

