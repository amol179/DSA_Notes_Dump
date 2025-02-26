def memo (p, n):
    
    
    for i in range(0, n):
        result.append(-2)

    return CUT_ROD(p, n, result)

def CUT_ROD(p, n, result):  # p is  the rice of the lengths of the rod
    # n is the length of the rod
    # result = []  # result store for each cuts made for length i

    if n == 0:
        return 0
    
    if result[n-1] >= 0:
        return result[n-1]
    q = -2
    
    for i in range(1, n +1):
            q = max(q, p[i - 1] + CUT_ROD(p, n-i, result)) # n - i for remaing len of rod
            
    print(q)
    
    result[n-1] = q
    
    print(result)
    
    return q
    
    
result = []

p = [1, 5, 8, 9, 10, 17]
n = 6 

ans = memo(p, n)

print (ans)