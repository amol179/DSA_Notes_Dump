T = int(input())  # Number of test cases
result = []  # List to store the results

for _ in range(T):
    A = input().strip()  # Input the binary string

    # Count the number of '1's in the string
    c = A.count('1')
    
    # Append the result of the current test case
    result.append(c)

# Print the results (the counts of '1's in each test case)
for count in result:
    print(count)
