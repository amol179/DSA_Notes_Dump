#Write a function using recursion to check if a number n is prime
#(you have to check whether n is divisible by any number below n). 

###################################################

def RecIsPrime(m):
    """Uses recursion to check if m is prime."""
    def PrimeHelper(m, j):
        """Helper Function to iterate through all j less than m up to 1 to look for even divisors."""
        if j == 1:  # Assume 1 is a prime number even though it's debatable.
            return True
        else:
            #do this task if both conditionals are true
            #else break and return false.
            return m % j != 0 and PrimeHelper(m, j - 1)
    return PrimeHelper(m, m -1)

# Tests
print( RecIsPrime(5))
print( RecIsPrime(6))
