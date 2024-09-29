T = int(input())
if T >= 1 and T <= 10:
    for _ in range(T):
        n = int(input())
        if n >= 1 and n <= 10 ^ 5:
            dolls = []
    for i in range(n):
        ele = int(input())
        if ele >= 1 and ele <= 10 ^ 5:
            dolls.append(ele)

    Account = {}
    for element in dolls:
        if element in Account:
            Account[element] += 1
        else:
            Account[element] = 1

    for element, count in Account.items():
        if count == 1:
            print(element)
