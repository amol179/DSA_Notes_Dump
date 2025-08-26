T = int(input())
for _ in range(T):
    D, d, P, Q = map(int, input().split())
    if D >= d and D <= 100:
        for days in range(D):
            interval = D // d  # interval of change
            remDay = D % d
            production = d * interval * (P + Q * (interval - 1) / 2)
            remDay_production = remDay * (P + interval * Q)

    print(int(production + remDay_production))
