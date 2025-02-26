def cut_rod(p,n):
    r = [0] * (n+1)
    
    for j in range(1, n+1):
        q = -2
        for i in range(1, j+1):
            q =  max(q, p[i-1] + r[j - i])
        r[j] = q
        
    return r[n]

p = [1, 5, 8, 9, 10, 17] 
n = 4

print (cut_rod(p,n))