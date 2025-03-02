def check(word):
    if word.isupper() or (word[0].islower() and word[1:].isupper()):
        return word.swapcase()
    else:
        return word


S = input().strip()
if len(S) == 1:
    result = S.swapcase()
else:
    result = check(S)
print(result)
