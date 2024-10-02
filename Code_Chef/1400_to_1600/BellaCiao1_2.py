T = int(input())
for _ in range(T):
    D, d, P, Q = map(int, input().split())

    interval = D // d  # interval of change
    remDay = D % d
    change_ofRate = P + Q * interval

    production = d * (P * interval + Q * ((interval - 1) * interval) // 2)
    remDay_production = remDay * change_ofRate

    print(int(production + remDay_production))
