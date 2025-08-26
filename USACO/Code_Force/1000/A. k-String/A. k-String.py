def K_string(k, s):
    hash = {}

    for char in s:
        if char in hash:
            hash[char] += 1
        else:
            hash[char] = 1

    for i in hash.values():
        if i % k != 0:
            return "-1"

    substring = ""
    for char, count in hash.items():
        substring += char * (count // k)

    result = substring * k
    return result


k = int(input())

s = input().strip()

print(K_string(k, s))
