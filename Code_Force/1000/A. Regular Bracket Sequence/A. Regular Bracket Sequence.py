def can_form_rbs(s):
    """
    Function to check if the sequence can become a Regular Bracket Sequence (RBS).
    """
    min_balance = 0  # Minimum possible balance
    max_balance = 0  # Maximum possible balance

    for char in s:
        if char == "(":
            min_balance += 1
            max_balance += 1
        elif char == ")":
            min_balance -= 1
            max_balance -= 1
        else:  # char == '?'
            min_balance -= 1  # Assume '?' is ')'
            max_balance += 1  # Assume '?' is '('

        # At any point, balance cannot go negative
        min_balance = max(min_balance, 0)

        if max_balance < 0:  # More ')' than '(' is not valid
            return "NO"

    # Sequence is valid if min_balance is 0 at the end
    return "YES" if min_balance == 0 else "NO"


def process_test_cases():
    """
    Function to handle multiple test cases efficiently.
    """
    t = int(input())  # Number of test cases
    results = []
    for _ in range(t):
        s = input()  # Read the sequence
        results.append(can_form_rbs(s))

    # Output all results at once
    print("\n".join(results))


# Run the program
process_test_cases()
