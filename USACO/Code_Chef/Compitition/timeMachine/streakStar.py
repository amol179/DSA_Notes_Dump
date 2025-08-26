def calculate_streak(arr):
    max_streak = 1
    current_streak = 1
    
    for i in range(1, len(arr)):
        if arr[i] >= arr[i-1]:
            current_streak += 1
        else:
            current_streak = 1
        max_streak = max(max_streak, current_streak)
    
    return max_streak

def max_streak_value(T, cases):
    results = []
    
    for case in cases:
        N, X, A = case
        
        # Calculate the base streak value
        base_streak = calculate_streak(A)
        max_streak = base_streak
        
        # Try multiplying each element by X once and calculate the streak
        for i in range(N):
            original_value = A[i]
            A[i] = original_value * X
            new_streak = calculate_streak(A)
            max_streak = max(max_streak, new_streak)
            A[i] = original_value  # Revert to original value
        
        results.append(max_streak)
    
    return results

# Input processing
Test = int(input())
cases = []

for _ in range(Test):
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    cases.append((N, X, A))

results = max_streak_value(Test, cases)
for result in results:
    print(result)
