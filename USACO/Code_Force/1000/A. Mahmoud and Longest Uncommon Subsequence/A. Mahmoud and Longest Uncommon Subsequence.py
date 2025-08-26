def longest_uncommon_subsequence(a, b):
    # If the strings are identical, there's no uncommon subsequence
    if a == b:
        return -1
    # Otherwise, the longest uncommon subsequence is the length of the longer string
    return max(len(a), len(b))


# Example usage
a = input().strip()
b = input().strip()
print(longest_uncommon_subsequence(a, b))
