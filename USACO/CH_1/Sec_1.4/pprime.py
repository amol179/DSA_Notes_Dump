"""
ID: amolgur1
LANG: PYTHON3
TASK: pprime
"""

def is_prime(n):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        # 6k +- 1 optimization
        i += w
        w = 6 - w
    return True

def generate_palindromes(a, b):
    result = []
    
    for length in range(1, 9): 
        half_len = (length + 1) // 2
        start = 10**(half_len - 1)
        end = 10**half_len
        for half in range(start, end):
            half_str = str(half)
            if length % 2 == 0:
                pal_str = half_str + half_str[::-1]
            else:
                pal_str = half_str + half_str[-2::-1]
            pal = int(pal_str)
            if pal > b:
                return result
            if pal >= a and is_prime(pal):
                result.append(pal)
    return result

with open("pprime.in", "r") as f:
    a, b = map(int, f.readline().split())

primes = generate_palindromes(a, b)

with open("pprime.out", "w") as f:
    for p in primes:
        f.write(f"{p}\n")