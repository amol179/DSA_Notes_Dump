"""
ID: amolgur1
LANG: PYTHON3
TASK: crypt1
"""


def is_valid(number, expected_length, allowed_set):

    s = str(number)
    if len(s) != expected_length:
        return False
    for ch in s:
        if ch not in allowed_set:
            return False
    return True


fin = open("crypt1.in", "r")
fout = open("crypt1.out", "w")

data = fin.read().strip().split()
n = int(data[0])
allowed = data[1:]
allowed_set = set(allowed)

count = 0


for a in allowed:
    for b in allowed:
        for c in allowed:
            multiplicand = int(a + b + c)
            for d in allowed:
                for e in allowed:
                    multiplier = int(d + e)
                    partial1 = multiplicand * (multiplier % 10)
                    partial2 = multiplicand * (multiplier // 10)

                    total = multiplicand * multiplier

                    if (
                        is_valid(partial1, 3, allowed_set)
                        and is_valid(partial2, 3, allowed_set)
                        and is_valid(total, 4, allowed_set)
                    ):
                        count += 1


fout.write(str(count) + "\n")


fin.close()
fout.close()
