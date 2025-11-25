"""
ID: amolgur1
LANG: PYTHON3
TASK: zerosum

"""

def generate_sequences(n):
    results = []

    def dfs(index, expr):
        if index > n:
            if evaluate(expr) == 0:
                results.append(expr)
            return
        for op in [' ', '+', '-']:
            dfs(index + 1, expr + op + str(index))

    def evaluate(expr):
        expr = expr.replace(' ', '')  # Handle digit concatenation
        total = 0
        current = ''
        sign = '+'
        i = 0

        while i < len(expr):
            if expr[i] in '+-':
                if current:
                    if sign == '+':
                        total += int(current)
                    else:
                        total -= int(current)
                sign = expr[i]
                current = ''
            else:
                current += expr[i]
            i += 1

        # Apply last number
        if current:
            if sign == '+':
                total += int(current)
            else:
                total -= int(current)

        return total

    dfs(2, '1')
    return sorted(results)


# 🌟 File I/O with `with` block — classic style
def main():
    with open('zerosum.in', 'r') as infile:
        n = int(infile.readline().strip())

    sequences = generate_sequences(n)

    with open('zerosum.out', 'w') as outfile:
        for seq in sequences:
            outfile.write(seq + '\n')


# 🚀 Run the program
main()