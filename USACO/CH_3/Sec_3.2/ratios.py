"""
ID: amolgur1
LANG: PYTHON3
TASK: ratios
"""


def read_input():
    with open("ratios.in", "r") as f:
        lines = f.readlines()
        goal = list(map(int, lines[0].split()))
        mix1 = list(map(int, lines[1].split()))
        mix2 = list(map(int, lines[2].split()))
        mix3 = list(map(int, lines[3].split()))
    return goal, mix1, mix2, mix3

def write_output(result):
    with open("ratios.out", "w") as f:
        if result is None:
            f.write("NONE\n")
        else:
            f.write(" ".join(map(str, result)) + "\n")

def is_valid_combo(goal, total):
    x, y, z = goal
    a, b, c = total

    # Avoid division by zero
    if x == 0 and a != 0: return False
    if y == 0 and b != 0: return False
    if z == 0 and c != 0: return False

    # Determine k from non-zero goal components
    k_vals = []
    if x != 0:
        if a % x != 0: return False
        k_vals.append(a // x)
    if y != 0:
        if b % y != 0: return False
        k_vals.append(b // y)
    if z != 0:
        if c % z != 0: return False
        k_vals.append(c // z)

    # All k values must be equal
    return all(k == k_vals[0] for k in k_vals)

def find_min_combo(goal, mix1, mix2, mix3):
    min_sum = 301  # max possible is 99+99+99
    best_combo = None

    for m1 in range(100):
        for m2 in range(100):
            for m3 in range(100):
                total_a = m1 * mix1[0] + m2 * mix2[0] + m3 * mix3[0]
                total_b = m1 * mix1[1] + m2 * mix2[1] + m3 * mix3[1]
                total_c = m1 * mix1[2] + m2 * mix2[2] + m3 * mix3[2]
                total = [total_a, total_b, total_c]

                if is_valid_combo(goal, total):
                    k = total_a // goal[0] if goal[0] != 0 else total_b // goal[1] if goal[1] != 0 else total_c // goal[2]
                    if m1 + m2 + m3 < min_sum and k > 0:
                        min_sum = m1 + m2 + m3
                        best_combo = [m1, m2, m3, k]

    return best_combo

def main():
    goal, mix1, mix2, mix3 = read_input()
    result = find_min_combo(goal, mix1, mix2, mix3)
    write_output(result)

main()