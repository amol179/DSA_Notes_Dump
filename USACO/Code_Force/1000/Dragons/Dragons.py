def can_kirito_win(s, dragons):
    while dragons:
        best_dragon_index = -1
        max_bonus = -1
        for i in range(len(dragons)):
            if s > dragons[i][0]:
                if dragons[i][1] > max_bonus:
                    best_dragon_index = i
                    max_bonus = dragons[i][1]

        if best_dragon_index == -1:
            return "NO"

        s += dragons[best_dragon_index][1]

        dragons.pop(best_dragon_index)

    return "YES"


def main():
    s, n = map(int, input().split())

    dragons = []
    for _ in range(n):
        xi, yi = map(int, input().split())
        dragons.append((xi, yi))

    result = can_kirito_win(s, dragons)
    print(result)


if __name__ == "__main__":
    main()
