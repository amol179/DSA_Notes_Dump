#https://www.codechef.com/practice/course/strings/STRINGS/problems/ADDONE


# Test = int(input())

# for _ in range(Test):
#     N = str(input())
#     result = int(N) + 1
#     print(str(result))

# NOTE : isse answer to ara hai code chef accept nahi krra
##########################################################

Test = int(input())

for _ in range(Test):
    N = list(map(int, input().split()))
    carry = 1
    for i in range(len(N) - 1, -1, -1):
        digit = int(N[i]) + carry
        
        if digit == 10:
            N[i] = '0'
            carry = 1
        else:
            N[i] = str(digit)
            carry = 0
    if carry == 1:
        N.insert(0, '1')
        
    print(''.join(N))
    