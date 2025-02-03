def solve():
    n = int(input())  # number of elements
    arr = list(map(int, input().split()))  # the array of integers
    
    # Variables to keep track of the best result
    max_len = 0
    left = 0
    sum_window = 0
    contains_negative = False
    
    for right in range(n):
        sum_window += arr[right]
        if arr[right] < 0:
            contains_negative = True
        
        # Shrink the window if the sum becomes negative
        while sum_window < 0 and left <= right:
            sum_window -= arr[left]
            if arr[left] < 0:
                contains_negative = False  # remove negative if we're excluding it
            left += 1
        
        # After shrinking the window, check if the conditions are satisfied
        if contains_negative and sum_window >= 0:
            max_len = max(max_len, right - left + 1)
    
    print(max_len)

# Read input and call the solve function
solve()
