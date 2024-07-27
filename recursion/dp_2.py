def cut_rod(prices , n):
    def memo(prices , n, m): #funcrion to memorize the max revenue 
        if n == 0:  #agar length 0 hai to return q ki revenue bhi 0
            return 0
        if m[n] >= 0:
            return m[n]
        
        
        q = -2
        
        for i in range(1, n+1): #for every i length in n , i is the fraction of n 
            q = max(q, prices[i - 1] + memo(prices, n - i, m)) # n-1 bachi hui rod hai i length pe cut krne k baad  
            
        print(q) 
        
        m[n] = q
        
        return q
    
    m = [-1] * (n + 1) #m ek array hai for storing max revenue, aur uska size is = n, aur har element ko -infinty set kiye intially
    
    print(m) #m ki values print krra
    
    return memo(prices, n, m)


prices = [1, 5, 8, 9, 10, 17]
n = 6 

ans = cut_rod(prices, n)

print(ans)
