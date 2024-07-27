
Test = int(input())

for _ in range(Test):
    Size = int(input())
    Array = list(map(int, input().split()))
    Min = min(Array)
    
    # jitne bar min repeat hora array me usko minus krenge
    # remaing no. is the number of operations. 
    print(Size - Array.count(Min))
    

