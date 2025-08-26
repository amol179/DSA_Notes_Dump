"""
ID: amolgur1
LANG: PYTHON3
TASK: sort3
"""

def minimal_exchanges(arr):
    # Step 1: Count how many of each key we have
    n1 = arr.count(1)
    n2 = arr.count(2)
    n3 = arr.count(3)

    # Step 2: Define segments
    segment1 = arr[:n1]          # Where all 1s should go
    segment2 = arr[n1:n1+n2]     # Where all 2s should go
    segment3 = arr[n1+n2:]       # Where all 3s should go

    # Step 3: Count misplaced elements
    c11 = segment1.count(1)
    c12 = segment1.count(2)
    c13 = segment1.count(3)

    c21 = segment2.count(1)
    c22 = segment2.count(2)
    c23 = segment2.count(3)

    c31 = segment3.count(1)
    c32 = segment3.count(2)
    c33 = segment3.count(3)

    # Step 4: Direct swaps
    swap12 = min(c12, c21)
    swap13 = min(c13, c31)
    swap23 = min(c23, c32)

    # Step 5: Remaining misplacements for cycle swaps
    leftover12 = c12 + c21 - 2 * swap12
    leftover13 = c13 + c31 - 2 * swap13
    leftover23 = c23 + c32 - 2 * swap23

    cycle_swaps = (leftover12 + leftover13 + leftover23) // 3 * 2

    return swap12 + swap13 + swap23 + cycle_swaps


with open('sort3.in', 'r') as fin:
    lines = fin.readlines()
    n = int(lines[0])
    arr = [int(x.strip()) for x in lines[1:n+1]]

result = minimal_exchanges(arr)

with open('sort3.out', 'w') as fout:
    fout.write(str(result) + '\n')