"""
ID: amolgur1
LANG: PYTHON3
TASK: palsquare
"""

fin = open("palsquare.in", "r")
B = int(fin.readline().strip())
fin.close()

digits = "0123456789ABCDEFGHIJ"

output_lines = []

for N in range(1, 301):
    square = N * N

    temp = square
    square_base = ""
    if temp == 0:
        square_base = "0"
    while temp > 0:
        remainder = temp % B
        square_base = digits[remainder] + square_base
        temp //= B

    if square_base == square_base[::-1]:
        temp = N
        N_base = ""
        if temp == 0:
            N_base = "0"
        while temp > 0:
            remainder = temp % B
            N_base = digits[remainder] + N_base
            temp //= B

        output_lines.append(N_base + " " + square_base + "\n")

fout = open("palsquare.out", "w")
fout.writelines(output_lines)
fout.close()
