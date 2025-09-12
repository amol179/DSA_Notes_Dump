"""
ID: amolgur1
LANG: PYTHON3
TASK:  fc
"""

def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def dist(a, b):
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    return (dx * dx + dy * dy) ** 0.5

def convex_hull(points):
    points.sort()
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]

def main():
    fin = open("fc.in", "r")
    lines = fin.readlines()
    fin.close()

    n = int(lines[0])
    if n == 0:
        result = 0.00
    else:
        points = []
        for i in range(1, n + 1):
            x, y = map(float, lines[i].strip().split())
            points.append((x, y))
        hull = convex_hull(points)
        perimeter = 0.0
        for i in range(len(hull)):
            perimeter += dist(hull[i], hull[(i + 1) % len(hull)])
        result = perimeter

    fout = open("fc.out", "w")
    fout.write("{:.2f}\n".format(result))
    fout.close()

main()