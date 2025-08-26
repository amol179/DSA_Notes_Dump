"""
ID: amolgur1
LANG: PYTHON3
TASK: fracdec

"""



def fracdec():
    with open("fracdec.in", "r") as fin:
        line = fin.readline().strip()
        N, D = map(int, line.split())

    # Integer part
    integer_part = N // D
    remainder = N % D

    # If there's no remainder, it's a whole number
    if remainder == 0:
        result = f"{integer_part}.0"
    else:
        decimal_digits = []
        seen_remainders = {}
        repeating_start = None

        position = 0
        while remainder != 0:
            if remainder in seen_remainders:
                repeating_start = seen_remainders[remainder]
                break
            seen_remainders[remainder] = position
            remainder *= 10
            digit = remainder // D
            decimal_digits.append(str(digit))
            remainder %= D
            position += 1

        if repeating_start is not None:
            non_repeating = ''.join(decimal_digits[:repeating_start])
            repeating = ''.join(decimal_digits[repeating_start:])
            result = f"{integer_part}.{non_repeating}({repeating})"
        else:
            result = f"{integer_part}." + ''.join(decimal_digits)

    # Split into lines of max 76 characters
    with open("fracdec.out", "w") as fout:
        for i in range(0, len(result), 76):
            fout.write(result[i:i+76] + "\n")

# Run the function
fracdec()
