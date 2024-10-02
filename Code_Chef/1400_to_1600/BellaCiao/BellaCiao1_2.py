T = int(input())
for _ in range(T):
    D, d, P, Q = map(int, input().split())

    interval = D // d  # complete interval of change
    remDay = D % d  # remaing day, incomplete cycle
    change_ofRate = P + Q * interval  # production rate

    production = d * (P * interval + Q * ((interval - 1) * interval) // 2)
    remDay_production = remDay * change_ofRate

    print(int(production + remDay_production))
