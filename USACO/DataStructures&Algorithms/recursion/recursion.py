#Recursion is an algorithmic technique where a function, in order to accomplish a task,
#calls itself with some part of the task. 
#adapted from MIT course:
#http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-189-a-gentle-introduction-to-programming-using-python-january-iap-2011/lectures/MIT6_189IAP11_rec_problems.pdf



#Non-recursive function
def it_sum(a_list):
    '''this function iterates over the values in the variable a list'''
    result = 0 
    for x in a_list: 
        result += x 
    return result 


x=it_sum([1,2,3,4,5])
print(x)

##################################################
#Sum
##################################################

def rec_sum(a_list):
    '''
    base case is when the list is empty
    The recursive case is demonstrated by calls to rec sum where the argument is a non-empty list
    '''
    if a_list == []: 
        return 0 
    else: 
        return a_list[0] + rec_sum(a_list[1:]) 


x=it_sum([1,2,3,4,5])
print(x)
##################################################
#Factorial
##################################################


def fact(n):
    # Recursive factorial definition
    if n < 0:
        # Error Check: (-n)!
        return "Error - no negetive guys."
    elif n == 0:
        # Base case: 0! = 1
        return 1
    else:
        # Recursive case: n! = n*(n-1)!
        #print (n * fact(n-1))
        return n * fact(n-1)

f=fact(5)
print(f)



##################################################
#Multiplication
##################################################

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

###################################################
#Exponentials
###################################################

def rExp(n,e):
    """recursively computes base^exp for non negetive numbers."""
    if e==0:  # Base case.
        return n
    else:
        return n * rExp(n,e-1) # Recursive case.

# Tests
print(rExp(2,3))


###################################################
#Write a function using recursion that takes in a string
#and returns a reversed copy of the string.	 The only 
#only use string concatenation.
###################################################


'''
first try the non-recursive way
'''
def rev(s):

    reverse=''
    for letter in s:
        reverse=letter+reverse
    return reverse

print(rev('oshmo'))

#Ankan Basu version of recursion method 
#for reversing a string

def r(s):
    #define the base case
    if s=='':
        return ''
    else:
        return s[len(s)-1]+r(s[0:len(s)-1])

print(r('ankan'))
print(r('oshmo'))


def rReverseString(input):
    """Reverse the input string using recursion."""
    if len(input) == 0:
        return ""
    else:
        return input[-1] + rReverseString(input[:-1])

# Tests
print(rReverseString('ankan'))
print(rReverseString('oshmo'))


###################################################
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


###################################################
#The Fibo Recursion
###################################################

def RecFib(n):
    """Returns the nth Fibonacci number."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return RecFib(n - 1) + RecFib(n - 2)

assert RecFib(3) == 2
assert RecFib(4) == 3