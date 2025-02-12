Test = int(input())

for _ in range(Test):
    X, Y = map(int, input().split())
    ones_half = '1' * (X // 2)
    twos_half = '2' * (Y // 2)
    first_half = ones_half + twos_half
    second_half = first_half[::-1]
    palindrome = first_half + second_half
    print(palindrome)
