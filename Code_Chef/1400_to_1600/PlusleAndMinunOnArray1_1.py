I = (int, input().split())
S = []
for i in range(len(I)):
    if i % 2 == 0:
        if i > 0:
            S.append((I[i]))
    else:
        S.append(I[i])
