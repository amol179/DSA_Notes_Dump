def partition(n, m=None):
    if m is None:
        m = n
    if n == 0:
        return 1
    if n < 0 or m == 0:
        return 0
    q = partition(n - m, m) + partition(n, m - 1)
    
    print(q)
    
    return (q)

# Example usage
n = 6
print("Number of partitions for n =", n, "is:", partition(n))
