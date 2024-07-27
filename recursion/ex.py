def memo (p, n):
    
    for i in range(0, n+1):
        result.append(-2)

    return CUT_ROD(p, n, result)

def CUT_ROD(p, n, result):  # p is  the rice of the lengths of the rod
    # n is the length of the rod
    # result = []  # result store for each cuts made for length i

    
    if result[n] >= 0:
        print ("hi")
        return result[n]
    
    if n == 0:
        return 0
    
    q = -2
    
    
    
    print(result)
    return result

result = []


p = [1, 5, 8, 9, 10, 17]
n = 6 

ans = memo(p, n)

print (ans)