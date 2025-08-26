def find_number(n, t):
    if t == 10:
        if n == 1:
            return -1
        else:
            return "1" + "0" * (n - 1)
    else:
        return str(t) + "0" * (n - 1 - len(str(t)) + 1)


n, t = map(int, input().split())
print(find_number(n, t))
