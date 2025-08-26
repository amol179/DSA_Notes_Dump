def main():
    t = int(input())
    for _ in range(t):
        a = input().strip()
        b = input().strip()

        max_common = 0
        len_a = len(a)

        # Iterating over all substrings of a
        for i in range(len_a):
            for j in range(i, len_a):
                substring = a[i : j + 1]
                # Check if the current substring is in b
                if substring in b:
                    # Update maximum common substring length
                    current_length = j - i + 1
                    if current_length > max_common:
                        max_common = current_length

        # Calculate the minimum number of operations:
        # (number of deletions in a) + (number of deletions in b)
        result = len(a) + len(b) - 2 * max_common
        print(result)


if __name__ == "__main__":
    main()
