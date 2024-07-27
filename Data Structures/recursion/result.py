result = []

bet = []

def CUT_ROD(p, n):  # p is  the rice of the lengths of the rod
    # n is the length of the rod
    #result = []  # result store for each cuts made for length i
    
    if n == 0:
        return 0

    q = -2  # max revenue for the length of the rod

    for i in range(1, n + 1):  # loop to check the maximum revenue genrated by cutting at different lengths.
        q = max(q, p[i - 1] + CUT_ROD(p, n - i))  # n - i for remaing len of rod
            
    if q not in result:
        result.append(q)  # adds elemments in the array of prices of made cuts.
        
        if i == k:
            print(q)
            
    return q

p = [1, 5, 8, 9, 10, 17]
n = 6

k = 3

ans = CUT_ROD(p,n)

print(result)


print(ans)