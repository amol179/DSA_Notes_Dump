"""
ID: amolgur1
LANG: PYTHON3
TASK: gift1
"""

# Read input file
with open("gift1.in", "r") as f:
    lines = f.read().splitlines()

ptr = 0
np = int(lines[ptr])
ptr += 1

names = [lines[ptr + i].strip() for i in range(np)]
ptr += np

balance = {name: 0 for name in names}

for _ in range(np):
    giver = lines[ptr].strip()
    ptr += 1
    amount, num_recipients = map(int, lines[ptr].split())
    ptr += 1
    recipients = []
    if num_recipients > 0:
        recipients = [lines[ptr + i].strip() for i in range(num_recipients)]
        ptr += num_recipients
    if num_recipients == 0:
        continue
    per_person = amount // num_recipients
    total_given = per_person * num_recipients
    balance[giver] -= total_given
    for recipient in recipients:
        balance[recipient] += per_person

# Write output file
with open("gift1.out", "w") as f:
    for name in names:
        f.write(f"{name} {balance[name]}\n")
