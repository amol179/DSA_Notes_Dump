"""
ID: amolgur1
LANG: PYTHON3
TASK: shuttle
"""

#!/usr/bin/env python3
# shuttle_fixed.py
# Reads N (either from shuttle.in or stdin) and prints the correct move sequence
# 20 numbers per line. Based on the standard USACO construction.

import sys

def read_N():
    # Try USACO file format first, otherwise read stdin
    try:
        with open("shuttle.in", "r") as f:
            data = f.read().strip().split()
            if data:
                return int(data[0])
    except Exception:
        pass
    data = sys.stdin.read().strip().split()
    if not data:
        raise ValueError("No input found")
    return int(data[0])

def generate_moves(N):
    p = N
    sig = 1
    moves = [p]

    # Increasing "staircase" part
    for i in range(1, N):
        for j in range(i):
            p += 2 * sig
            moves.append(p)
        p += sig
        moves.append(p)
        sig = -sig

    # Middle block
    for i in range(N):
        p += 2 * sig
        moves.append(p)

    sig = -sig

    # Symmetric decreasing part
    for i in range(N - 1, 0, -1):
        p += sig
        moves.append(p)
        for j in range(i):
            p += 2 * sig
            moves.append(p)
        sig = -sig

    # final decrement (matching the C++/classic implementation)
    p -= 1
    moves.append(p)
    return moves

def write_output(moves):
    # Try writing to shuttle.out (USACO), but always print to stdout as well.
    out_lines = []
    line = []
    for i, val in enumerate(moves, start=1):
        line.append(str(val))
        if i % 20 == 0:
            out_lines.append(" ".join(line))
            line = []
    if line:
        out_lines.append(" ".join(line))

    out_text = "\n".join(out_lines) + "\n"

    try:
        with open("shuttle.out", "w") as f:
            f.write(out_text)
    except Exception:
        pass

    sys.stdout.write(out_text)

def main():
    N = read_N()
    moves = generate_moves(N)
    # the correct total number of moves is N*(N+2)
    expected = N * (N + 2)
    if len(moves) != expected:
        # safety: trim or extend (shouldn't be necessary)
        moves = moves[:expected]
    write_output(moves)

if __name__ == "__main__":
    main()
