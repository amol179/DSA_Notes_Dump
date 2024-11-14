t = int(input())
for i in range(t):
    N = int(input())
    A = list(map(int, input().split()))
    i = 0
    j = N - 1
    pro_1 = 0
    pro_2 = 0
    while i <= j:
        if pro_1 < pro_2:
            pro_1 += A[i]
            i += 1
        else:
            pro_2 += A[j]
            j -= 1
    print(max(pro_1, pro_2))
