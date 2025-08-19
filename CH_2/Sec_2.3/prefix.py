"""
ID: amolgur1
LANG: PYTHON3
TASK: prefix
"""



with open("prefix.in", "r") as f:
    lines = f.readlines()

primitives = []
sequence_lines = []
reading_primitives = True

for line in lines:
    line = line.strip()
    if reading_primitives:
        if line == ".":
            reading_primitives = False
        else:
            primitives.extend(line.split())
    else:
        sequence_lines.append(line)

sequence = "".join(sequence_lines)
max_len = len(sequence)
dp = [False] * (max_len + 1)
dp[0] = True  # Empty prefix is always constructible

for i in range(max_len + 1):
    if dp[i]:
        for p in primitives:
            end = i + len(p)
            if end <= max_len and sequence[i:end] == p:
                dp[end] = True

    # Find longest prefix where dp[i] is True
result = 0
for i in range(max_len + 1):
    if dp[i]:
        result = i

with open("prefix.out", "w") as f:
    f.write(str(result) + "\n")

