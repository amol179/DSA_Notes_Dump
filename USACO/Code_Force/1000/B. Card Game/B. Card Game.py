def count_suneet_wins(a1, a2, b1, b2):
    # All possible combinations of rounds
    combinations = [(a1, b1), (a1, b2), (a2, b1), (a2, b2)]
    suneet_wins = 0

    # Iterate over each combination of rounds
    for comb in combinations:
        suneet_score = 0
        slavic_score = 0

        # First round
        if comb[0] > comb[1]:
            suneet_score += 1
        elif comb[0] < comb[1]:
            slavic_score += 1

        # Second round (remaining cards)
        remaining_suneet = a1 + a2 - comb[0]
        remaining_slavic = b1 + b2 - comb[1]
        if remaining_suneet > remaining_slavic:
            suneet_score += 1
        elif remaining_suneet < remaining_slavic:
            slavic_score += 1

        # Check game winner
        if suneet_score > slavic_score:
            suneet_wins += 1

    return suneet_wins


# Input and Output
t = int(input())  # Number of test cases
results = []

for _ in range(t):
    a1, a2, b1, b2 = map(int, input().split())
    results.append(count_suneet_wins(a1, a2, b1, b2))

for res in results:
    print(res)
