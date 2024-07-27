# Read the first line containing N and X
N, X = map(int, input().strip().split())

# Read the second line containing N space-separated integers and store them in list A
A = list(map(int, input().strip().split()))

# Check if X is in the list A
if X in A:
    print("YES")
else:
    print("NO")
