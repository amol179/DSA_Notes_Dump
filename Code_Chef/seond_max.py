# no of elements
N = int(input())

# Process each set of three integers
for _ in range(N):
    # Read the three integers
    a, b, c = map(int, input().split())
    # Find the second largest number
    second_max = sorted([a, b, c])[1]
    # Print the result
    print(second_max)

