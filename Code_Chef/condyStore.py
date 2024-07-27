#https://www.codechef.com/practice/course/basic-math/BASICMATH/problems/CANDYSTORE

Test = int(input())

for _ in range(Test):
    X, Y = map(int, input().split())
    
    for i in range(X):
        if X >= Y:
            rev = 1 * Y
        elif X < Y:
            rev = X * 1 + (Y - X) * 2
    
    print(rev)
        


