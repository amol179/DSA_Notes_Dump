n = int(input())
p = list(map(int, input().split()))
q = [0] * n
for i in range(n):
    recipient = p[i]
    q[recipient - 1] = i + 1
print(" ".join(map(str, q)))
