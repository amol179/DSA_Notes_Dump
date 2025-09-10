"""
ID: amolgur1
LANG: PYTHON3
TASK: lgame

"""

# lgame.py

# Correct scoring table
values = {
    'a': 2, 'b': 5, 'c': 4, 'd': 4, 'e': 1, 'f': 6, 'g': 5, 'h': 5,
    'i': 1, 'j': 7, 'k': 6, 'l': 2, 'm': 5, 'n': 2, 'o': 3, 'p': 5,
    'q': 7, 'r': 2, 's': 1, 't': 3, 'u': 4, 'v': 6, 'w': 7, 'x': 7,
    'y': 5, 'z': 7
}

# -----------------------
# Helpers
# -----------------------

def count_letters(word):
    freq = {}
    for c in word:
        freq[c] = freq.get(c, 0) + 1
    return freq

def can_form(word_count, letters_count):
    for c in word_count:
        if word_count[c] > letters_count.get(c, 0):
            return False
    return True

def score_word(word):
    return sum(values[c] for c in word)

# -----------------------
# Main
# -----------------------

# Read input letters
with open("lgame.in", "r") as f:
    letters = f.readline().strip()

letters_count = count_letters(letters)

# Read dictionary strictly until "."
dictionary = []
with open("lgame.dict", "r") as f:
    for line in f:
        w = line.strip()
        if w == ".":
            break
        if 3 <= len(w) <= 7:
            wc = count_letters(w)
            if can_form(wc, letters_count):
                dictionary.append(w)

# Precompute counts and scores
word_info = []
for w in dictionary:
    word_info.append((w, count_letters(w), score_word(w)))

max_score = 0
results = []

# --- Single words ---
for w, wc, sc in word_info:
    if sc > max_score:
        max_score = sc
        results = [w]
    elif sc == max_score:
        results.append(w)

# --- Word pairs ---
n = len(word_info)
for i in range(n):
    w1, c1, s1 = word_info[i]
    for j in range(i, n):
        w2, c2, s2 = word_info[j]

        combined = {}
        for c in c1:
            combined[c] = combined.get(c, 0) + c1[c]
        for c in c2:
            combined[c] = combined.get(c, 0) + c2[c]

        if can_form(combined, letters_count):
            total = s1 + s2
            if total > max_score:
                max_score = total
                results = [w1 + " " + w2]
            elif total == max_score:
                results.append(w1 + " " + w2)

# Sort results alphabetically
results.sort()

# Write output
with open("lgame.out", "w") as f:
    f.write(str(max_score) + "\n")
    for r in results:
        f.write(r + "\n")
