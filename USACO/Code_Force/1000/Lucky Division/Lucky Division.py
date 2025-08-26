def is_lucky_number(number):
    while number > 0:
        digit = number % 10
        if digit != 4 and digit != 7:
            return False
        number //= 10
    return True


def find_lucky_numbers(limit):
    lucky_numbers = []
    for i in range(1, limit + 1):
        if is_lucky_number(i):
            lucky_numbers.append(i)
    return lucky_numbers


def is_almost_lucky(n):
    lucky_numbers = find_lucky_numbers(n)
    for lucky in lucky_numbers:
        if n % lucky == 0:
            return True
    return False


# Replace 'n' with your custom input
n = int(input())
if is_almost_lucky(n):
    print("YES")
else:
    print("NO")
