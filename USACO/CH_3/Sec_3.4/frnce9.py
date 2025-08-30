"""
ID: amolgur1
LANG: PYTHON3
TASK:  fence9
"""

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def main():
    # Read input
    with open("fence9.in", "r") as f:
        n, m, p = map(int, f.readline().split())

    # Step 1: Area of triangle
    area = (p * m) // 2

    # Step 2: Boundary points
    b1 = gcd(n, m)
    b2 = gcd(abs(p - n), m)
    b3 = p
    boundary = b1 + b2 + b3

    # Step 3: Pick's Theorem
    interior = area - boundary // 2 + 1

    # Write output
    with open("fence9.out", "w") as f:
        f.write(str(interior) + "\n")

main()