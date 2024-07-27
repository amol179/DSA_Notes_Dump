#https://www.codechef.com/practice/course/basic-math/BASICMATH/problems/FLOW002

Test = int(input())

for _ in range(Test):
    i, j = map(int, input().split())
    rem = i%j
    print (rem)
