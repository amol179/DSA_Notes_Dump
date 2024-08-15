Test = int(input())

for _ in range(Test):
    X, Y, Z = map(int,input().split())
    if X != Y and Y != Z and X != Z:
        print('YES')
    else:
        print('NO')