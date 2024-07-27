
t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    
    freshness = list(map(int, input().split()))
    cost = list(map(int, input().split()))
    
    # Calculate total cost
    total_cost = 0
    for i in range(n):
        if freshness[i] >= x:
            total_cost += cost[i]
    
    print(total_cost)
