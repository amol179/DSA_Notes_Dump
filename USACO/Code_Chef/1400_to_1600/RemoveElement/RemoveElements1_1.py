t = int(input())
for _ in range(t):
    N, K = map(int, input().split())
    A = [int(x) for x in input().split()]
    B = sorted(A)

    i = 0
    if len(B) == 1:
        print("YES")
    elif len(B) > 1:
        while i < len(B) - 1:
            sum = B[i] + B[i + 1]
            if sum <= K:
                B.remove(B[i + 1])
            else:

                break
        if len(B) == 1:
            print("YES")
        else:
            print("NO")
