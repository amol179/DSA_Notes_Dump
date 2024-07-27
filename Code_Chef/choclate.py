def max_chocolates(X, Y, Z):
    # Calculate the total money Chef has
    total_money = (X * 5) + (Y * 10)
    # Calculate the maximum number of chocolates Chef can buy
    return total_money // Z  # Integer division

# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Read X, Y, Z values for the test case
    X, Y, Z = map(int, input().split())
    # Compute and print the result for the current test case
    print(max_chocolates(X, Y, Z))
