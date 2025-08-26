"""
ID: amolgur1
LANG: PYTHON3
TASK: friday
"""

n = int(open("friday.in").read())
counts = [0] * 7

currentDay = 5


def Leap(year):
    if year % 100 == 0:
        return year % 400 == 0
    else:
        return year % 4 == 0


for year in range(1900, 1900 + n):
    for month in range(12):
        counts_index = (currentDay + 2) % 7
        counts[counts_index] += 1

        if month == 1:
            if Leap(year):
                days = 29
            else:
                days = 28
        elif month in [3, 5, 8, 10]:
            days = 30
        else:
            days = 31

        currentDay = (currentDay + days) % 7


with open("friday.out", "w") as fout:
    fout.write(" ".join(map(str, counts)) + "\n")
