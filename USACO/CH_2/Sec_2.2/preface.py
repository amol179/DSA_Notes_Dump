"""
ID: amolgur1
LANG: PYTHON3
TASK: preface
"""

def to_roman(num):
    result = ""
    values = [1000, 900, 500, 400, 100, 90, 50, 40,
              10, 9, 5, 4, 1]
    numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL",
                "X", "IX", "V", "IV", "I"]

    for i in range(len(values)):
        while num >= values[i]:
            result += numerals[i]
            num -= values[i]
    return result

with open("preface.in", "r") as fin:
    N = int(fin.readline().strip())

    # Initialize counter
counter = {
    'I': 0, 'V': 0, 'X': 0, 'L': 0,
    'C': 0, 'D': 0, 'M': 0
}

    # Count numerals
for i in range(1, N + 1):
    roman = to_roman(i)
    for ch in roman:
        counter[ch] += 1

    # Write output
order = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
with open("preface.out", "w") as fout:
    for ch in order:
        if counter[ch] > 0:
            fout.write(ch + " " + str(counter[ch]) + "\n")

