a = int(input())
b = int(input())
c = int(input())
ans = []
p = a + b * c
ans.append(p)
q = a * (b + c)
ans.append(q)
r = a * b * c
ans.append(r)
s = (a + b) * c
ans.append(s)
t = a + b + c
ans.append(t)

M = max(ans)
print(M)
