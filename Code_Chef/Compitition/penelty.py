def penalty_shootout(T, cases):
    results = []
    for X, Y in cases:
        turns_A = 5 - 3
        turns_B = 5 - 4
    
        max_A = X + turns_A
        max_B = Y + turns_B
        
        if max_A == max_B:
            results.append("YES")
        else:
            results.append("NO")
    
    return results

# Reading input
T = int(input().strip())
cases = []
for _ in range(T):
    X, Y = map(int, input().strip().split())
    cases.append((X, Y))

# Calling the function
results = penalty_shootout(T, cases)

# Output results
for result in results:
    print(result)
