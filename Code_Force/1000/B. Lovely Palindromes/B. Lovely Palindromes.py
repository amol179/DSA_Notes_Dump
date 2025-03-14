def nth_even_length_palindrome(n):
    # n is input as a string to handle its massive size
    prefix = n  # Use the prefix as-is
    # Mirror the prefix to form the palindrome
    palindrome = prefix + prefix[::-1]
    return palindrome


# Input
n = input().strip()  # Read the input as a string to support large values
# Output
print(nth_even_length_palindrome(n))
