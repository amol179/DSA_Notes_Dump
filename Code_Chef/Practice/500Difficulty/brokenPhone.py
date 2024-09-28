t = int(input())
for _ in range (t):
    R, N = map(int, input().split())
    if R < N:
        print('REPAIR')
    if R > N:
        print('NEW PHONE')
    if R == N:
        print('ANY')