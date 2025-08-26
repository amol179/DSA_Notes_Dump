"""
ID: amolgur1
LANG: PYTHON3
TASK: wormhole
"""


def read_input(filename="wormhole.in"):

    with open(filename, "r") as f:
        data = f.read().strip().split()
    N = int(data[0])
    wormholes = []
    for i in range(N):
        x = int(data[2 * i + 1])
        y = int(data[2 * i + 2])
        wormholes.append((x, y))
    return N, wormholes


def write_output(result, filename="wormhole.out"):

    with open(filename, "w") as f:
        f.write(str(result) + "\n")


def compute_next_on_right(N, wormholes):
    """
    right wala wormhole +x wala, if not -1
    """
    next_on_right = [-1] * N

    for i in range(N):
        xi, yi = wormholes[i]
        for j in range(N):
            xj, yj = wormholes[j]
            if yj == yi and xj > xi:
                if (
                    next_on_right[i] == -1
                    or xj - xi < wormholes[next_on_right[i]][0] - xi
                ):
                    next_on_right[i] = j
    return next_on_right


def cycle_exists(N, pairings, next_on_right):

    for start in range(N):
        pos = start

        for _ in range(N):
            nxt = next_on_right[pos]
            if nxt == -1:
                break

            pos = pairings[nxt]
        else:
            return True
    return False


def generate_pairings(N, pairings, used, next_on_right, total):

    i = None
    for idx in range(N):
        if not used[idx]:
            i = idx
            break

    if i is None:
        if cycle_exists(N, pairings, next_on_right):
            total[0] += 1
        return

    used[i] = True
    for j in range(i + 1, N):
        if not used[j]:
            used[j] = True

            pairings[i] = j
            pairings[j] = i

            generate_pairings(N, pairings, used, next_on_right, total)

            used[j] = False
    used[i] = False


N, wormholes = read_input()

next_on_right = compute_next_on_right(N, wormholes)

pairings = [-1] * N
used = [False] * N


total = [0]

generate_pairings(N, pairings, used, next_on_right, total)

write_output(total[0])
