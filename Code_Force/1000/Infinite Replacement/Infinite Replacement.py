def infinite_replacement(q, test_cases):
    results = []
    for i in range(q):
        s, t = test_cases[i]
        if t == "a":
            results.append(1)
        elif "a" in t:
            results.append(-1)
        else:
            results.append(2 ** len(s))
    return results


# Main function to handle input and output
def main():
    q = int(input().strip())
    test_cases = []
    for _ in range(q):
        s = input().strip()
        t = input().strip()
        test_cases.append((s, t))

    results = infinite_replacement(q, test_cases)
    for result in results:
        print(result)


# Example usage with custom input
if __name__ == "__main__":
    main()
