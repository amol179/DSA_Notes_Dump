for _ in range(int(input())):
    S = input()
    count = 0
    for i in range(len(S) - 1):
        if S[i] == S[i + 1]:
            count += 1
            break
    if count > 0:
        print(count)
    else:
        print(len(S))
