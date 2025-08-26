def digit_sum_transformations(n):
    count = 0
    while len(n) > 1:
        n = str(sum(int(digit) for digit in n))  # Compute sum of digits
        count += 1
    return count


# Example usage:
n = input().strip()  # Read input as a string to handle large numbers
print(digit_sum_transformations(n))
