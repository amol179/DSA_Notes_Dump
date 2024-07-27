Test =  int(input())

for _ in range(Test):
    N = int(input()) #size of array 
    A = list(map(int, input().split()))
    freq = {}
    
    for num in A:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
            
    target_value = max(freq, key=freq.get)
    
    total_cost = 0
    operation = []
    N = len(A)
    
    i = 0
    
    while i < N:
        if A[i] != target_value:
            L = i + 1
            
            while i < N and A[i] != target_value:
                i += 1
            R = i
            x = target_value
            cost = (R - L + 1) * x
            
            for j in range(L - 1, R):
                A[j] = x
                
            operation.append((L, R, x))
            total_cost += cost
            
        else:
            i += 1
            
    print(A)
            
            
    

   
    
    