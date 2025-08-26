def minimum_additional_walks(n, k, a):
    b = a.copy()
    additional_walks = 0

    for i in range(1, n):
        if b[i - 1] + b[i] < k:
            additional_walks_needed = k - (b[i - 1] + b[i])
            b[i] += additional_walks_needed
            additional_walks += additional_walks_needed

    return additional_walks, b


def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    additional_walks, b = minimum_additional_walks(n, k, a)
    print(additional_walks)
    print(" ".join(map(str, b)))


if __name__ == "__main__":
    main()
