t = int(input())

for _ in range(t):
    x = int(input())
    y = x + 1
    
    while True:
        # Check if y is prime
        if y > 1:
            is_prime = True
            if y % 2 == 0 and y > 2:
                is_prime = False
            else:
                for i in range(3, int(y ** 0.5) + 1, 2):
                    if y % i == 0:
                        is_prime = False
                        break
        else:
            is_prime = False
        
        # Check if y is a perfect square
        root = int(y ** 0.5)
        is_perfect_square = root * root == y

        if not is_prime and not is_perfect_square:
            valid = True
            for i in range(2, int(y ** 0.5) + 1):
                if y % i == 0 and i < x:
                    valid = False
                    break
            if valid:
                print(y)
                break
        y += 1
