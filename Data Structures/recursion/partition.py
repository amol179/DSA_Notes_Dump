def partition(n, m=None):
    if m is None:
        m = n
    if n == 0:
        return 1
    if n < 0 or m == 0:
        return 0
        
    print (partition(n - m, m) + partition(n, m - 1)) 

    return partition(n - m, m) + partition(n, m - 1)

# Example usage
n = 4
print("Number of partitions for n =", n, "is:", partition(n))
