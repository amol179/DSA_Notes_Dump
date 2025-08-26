"""
ID: amolgur1
LANG: PYTHON3
TASK: ride
"""

with open("ride.in", "r") as fin:
    comet_name = fin.readline().strip()
    group_name = fin.readline().strip()


def product_value(name):
    product = 1
    for letter in name:
        product *= ord(letter) - ord("A") + 1
    return product


comet_product = product_value(comet_name)
group_product = product_value(group_name)

comet_mod = comet_product % 47
group_mod = group_product % 47

if comet_mod == group_mod:
    result = "GO"
else:
    result = "STAY"

with open("ride.out", "w") as fout:
    fout.write(result + "\n")
