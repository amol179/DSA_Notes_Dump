#https://www.codechef.com/practice/course/arrays/ARRAYS/problems/UWCOI20A

Test = int(input())

for _ in range(Test):
    N = int(input())
    max_value = 0
    
    for _ in range(N):
        height = int(input())
        if height > max_value:
            max_value = height
            
    print(max_value)
    # print agar for loop k bahar kara to bhi answer to same hai
    # par codechef accept nahi krra tha 

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Test = int(input())

arr_len = int(input())
arr = []

for i in range(arr_len):
    A = int(input())
    arr.append(A)
    max_value = arr[0]
    for num in arr[1:]:
        if num > max_value:
            max_value = num


print(max_value)
    

