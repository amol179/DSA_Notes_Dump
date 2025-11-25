"""
ID: amolgur1
LANG: PYTHON3
TASK: runround
"""

def is_runaround(number):
    digits = str(number)
    length = len(digits)

    # Check for zero or repeated digits
    if '0' in digits or len(set(digits)) != length:
        return False

    visited = [False] * length
    index = 0

    for _ in range(length):
        if visited[index]:
            return False
        visited[index] = True
        step = int(digits[index])
        index = (index + step) % length

    return index == 0 and all(visited)

def find_next_runaround(M):
    number = M + 1
    while True:
        if is_runaround(number):
            return number
        number += 1



with open('runround.in', 'r') as infile:
    M = int(infile.readline().strip())


result = find_next_runaround(M)


with open('runround.out', 'w') as outfile:
    outfile.write(str(result) + '\n')

