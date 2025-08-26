"""
ID: amolgur1
LANG: PYTHON3
TASK: dualpal
"""


def convert_to_base(num, base):
    if num == 0:
        return "0"
    digits = []
    while num > 0:
        remainder = num % base
        digits.append(str(remainder))
        num = num // base
    return "".join(reversed(digits))


def is_palindrome(s):
    return s == s[::-1]


def dual_palindromes(N, S):
    results = []
    current = S + 1
    while len(results) < N:
        count = 0
        for base in range(2, 11):
            s = convert_to_base(current, base)
            if is_palindrome(s):
                count += 1
                if count >= 2:
                    break
        if count >= 2:
            results.append(current)
        current += 1
    return results


with open("dualpal.in", "r") as f:
    N, S = map(int, f.readline().split())
results = dual_palindromes(N, S)
with open("dualpal.out", "w") as f:
    for num in results:
        f.write(f"{num}\n")
