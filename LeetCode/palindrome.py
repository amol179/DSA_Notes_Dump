def longest_palindromic_substring(s):
    n = len(s)  #input string length 
    if n == 0:
        return ""

    # initialize empty box to store the values thare are already palindrome
    is_palindrome = [[False] * n for _ in range(n)]

    # start 
    start = 0
    max_length = 1

    # Single characters are always palindromes
    for i in range(n):
        is_palindrome[i][i] = True

    # Check for palindromes of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            is_palindrome[i][i + 1] = True
            start = i
            max_length = 2

    # Check for palindromes of length > 2
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and is_palindrome[i + 1][j - 1]:
                is_palindrome[i][j] = True
                start = i
                max_length = length

    return s[start:start + max_length]

# Example usage:
s = "babad"
print("Longest palindromic substring:", longest_palindromic_substring(s))
