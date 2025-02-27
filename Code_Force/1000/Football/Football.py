# Read input
n = int(input())
goals = [input().strip() for _ in range(n)]

# Count goals for each team
goal_count = {}
for team in goals:
    if team in goal_count:
        goal_count[team] += 1
    else:
        goal_count[team] = 1

# Determine the winning team
winner = max(goal_count, key=goal_count.get)
print(winner)
