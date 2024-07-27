# Write a function that takes in two numbers and recursively multiplies them together. 
 
def rMult(n1, n2):
    """Takes in two nonnegative numbers  and recursively multiplies them together."""
    if n1 == 1:  # Base case.
        return n2
    elif n1 == 0: # Always be 0.
        return 0
    else:
        return n2 + rMult(n1 - 1, n2) # Recursive case.

# Tests
print(rMult(5,4))
