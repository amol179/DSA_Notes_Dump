

t = int(input())

for _ in range(t):
    test_case = list(map(int, input().split()))
    result = []
    for case in test_case:
        n = case[0]
        array = case[1]
        
        # Calculate bitwise OR of all elements in the array
        bitwise_or = 0
        for num in array:
            bitwise_or |= num
        
        min_removals = n
        
        x = 0
        while (1 << x) - 1 <= 10**9:  # 2^x - 1 should not exceed 10^9 as per the constraints
            desired_or_value = (1 << x) - 1
            if desired_or_value >= bitwise_or:
                min_removals = min(min_removals, n - 1)
            x += 1
        
        result.append(min_removals)
        
    print(result)