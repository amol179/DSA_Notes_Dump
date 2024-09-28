T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    cap = x * 5
    if cap >= y:
        print('YES')
        
    else:
        print('NO')