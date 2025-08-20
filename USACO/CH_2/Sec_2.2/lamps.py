"""
ID: amolgur1
LANG: PYTHON3
TASK: lamps
"""

def toggle(state, indices):
    for i in indices:
        state[i] ^= 1

def button_effects(n):
    return {
        1: list(range(n)),                      # Button 1: all lamps
        2: [i for i in range(n) if (i + 1) % 2 == 1],  # Button 2: odd lamps
        3: [i for i in range(n) if (i + 1) % 2 == 0],  # Button 3: even lamps
        4: [i for i in range(n) if (i % 3 == 0)]       # Button 4: 3xK+1 (i = 0,3,6,...)
    }

def apply_buttons(n, button_combo):
    state = [1] * n  # all ON initially
    effects = button_effects(n)
    for b in button_combo:
        toggle(state, effects[b])
    return state

def satisfies_constraints(state, on_lamps, off_lamps):
    for i in on_lamps:
        if state[i - 1] != 1:
            return False
    for i in off_lamps:
        if state[i - 1] != 0:
            return False
    return True

def generate_combinations():
    combos = []
    for i in range(16):  # 2^4 possibilities
        combo = []
        for j in range(4):
            if (i >> j) & 1:
                combo.append(j + 1)
        combos.append(combo)
    return combos


with open('lamps.in', 'r') as fin:
    n = int(fin.readline())
    c = int(fin.readline())
    on_lamps = list(map(int, fin.readline().split()))
    off_lamps = list(map(int, fin.readline().split()))
    on_lamps = [x for x in on_lamps if x != -1]
    off_lamps = [x for x in off_lamps if x != -1]

seen = set()
valid_configs = []

for combo in generate_combinations():
    press_count = len(combo)
    if press_count <= c and (c - press_count) % 2 == 0:
        state = apply_buttons(n, combo)
        if satisfies_constraints(state, on_lamps, off_lamps):
            config = ''.join(map(str, state))
            if config not in seen:
                seen.add(config)
                valid_configs.append(config)

valid_configs.sort()

with open('lamps.out', 'w') as fout:
    if not valid_configs:
        fout.write('IMPOSSIBLE\n')
    else:
        for config in valid_configs:
            fout.write(config + '\n')
