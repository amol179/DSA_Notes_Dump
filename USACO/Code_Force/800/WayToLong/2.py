N = int(input())

results = []

for _ in range(N):
    Word = input()
    L = len(Word)

    if L > 10:
        Abv = Word[0] + str(len(Word) - 2) + Word[-1]
        results.append(Abv)
    else:
        results.append(Word)

for result in results:
    print(result)
