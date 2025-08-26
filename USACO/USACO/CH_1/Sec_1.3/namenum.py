"""
ID: amolgur1
LANG: PYTHON3
TASK: namenum
"""

with open("namenum.in", "r") as fin:
    target_num = fin.readline().strip()

with open("dict.txt", "r") as fdict:
    words = [line.strip() for line in fdict.readlines()]


char_to_digit = {
    "A": "2",
    "B": "2",
    "C": "2",
    "D": "3",
    "E": "3",
    "F": "3",
    "G": "4",
    "H": "4",
    "I": "4",
    "J": "5",
    "K": "5",
    "L": "5",
    "M": "6",
    "N": "6",
    "O": "6",
    "P": "7",
    "R": "7",
    "S": "7",
    "T": "8",
    "U": "8",
    "V": "8",
    "W": "9",
    "X": "9",
    "Y": "9",
}


matches = []
target_len = len(target_num)

for word in words:
    if len(word) != target_len:
        continue
    current_num = []
    valid = True

    for c in word:
        if c not in char_to_digit:
            valid = False
            break

        current_num.append(char_to_digit[c])
    if not valid:
        continue
    generated_num = "".join(current_num)
    if generated_num == target_num:
        matches.append(word)

with open("namenum.out", "w") as fout:
    if not matches:
        fout.write("NONE\n")
    else:
        for name in matches:
            fout.write(f"{name}\n")
