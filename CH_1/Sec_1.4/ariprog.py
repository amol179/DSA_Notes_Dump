"""
ID: amolgur1
LANG: PYTHON3
TASK: ariprog
"""


def find_sequences(N, M):
    bisquares = set()
    max_val = 2 * M * M

    for p in range(M + 1):
        p2 = p * p
        for q in range(M + 1):
            bisquares.add(p2 + q * q)

    bisquares_list = sorted(list(bisquares))

    is_bisquare = [False] * (max_val + 1)
    for x in bisquares_list:
        is_bisquare[x] = True

    sequences = []

    bisquares_len = len(bisquares_list)

    max_start = max_val - (N - 1)

    left, right = 0, bisquares_len - 1
    while left <= right:
        mid = (left + right) // 2
        if bisquares_list[mid] > max_start:
            right = mid - 1
        else:
            left = mid + 1
    max_start_idx = right

    for i in range(max_start_idx + 1):
        start = bisquares_list[i]

        max_diff = (max_val - start) // (N - 1)

        for j in range(i + 1, bisquares_len):
            diff = bisquares_list[j] - start

            if diff > max_diff:
                break

            last_val = start + (N - 1) * diff
            if last_val > max_val or not is_bisquare[last_val]:
                continue

            valid = True
            for k in range(1, N - 1):
                if not is_bisquare[start + k * diff]:
                    valid = False
                    break

            if valid:
                sequences.append((start, diff))

    return sequences


with open("ariprog.in", "r") as fin:
    N = int(fin.readline().strip())
    M = int(fin.readline().strip())

sequences = find_sequences(N, M)

with open("ariprog.out", "w") as fout:
    if not sequences:
        fout.write("NONE\n")
    else:
        sequences.sort(key=lambda x: (x[1], x[0]))
        for start, diff in sequences:
            fout.write(f"{start} {diff}\n")
