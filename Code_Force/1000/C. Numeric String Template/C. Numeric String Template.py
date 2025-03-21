def is_matching_template(array, string):
    if len(array) != len(string):
        return False

    mapping_a_to_s = {}
    mapping_s_to_a = {}

    for i in range(len(array)):
        num = array[i]
        char = string[i]

        if num in mapping_a_to_s and mapping_a_to_s[num] != char:
            return False
        if char in mapping_s_to_a and mapping_s_to_a[char] != num:
            return False

        mapping_a_to_s[num] = char
        mapping_s_to_a[char] = num

    return True


def main():
    t = int(input())  # Number of test cases
    results = []

    for _ in range(t):
        n = int(input())  # Length of the array
        array = list(map(int, input().split()))  # Template array
        m = int(input())  # Number of strings to check
        strings = [input().strip() for _ in range(m)]

        for string in strings:
            if is_matching_template(array, string):
                results.append("YES")
            else:
                results.append("NO")

    print("\n".join(results))


if __name__ == "__main__":
    main()
