"""
ID: amolgur1
LANG: PYTHON3
TASK: spin
"""

def read_input():
    wheels = []
    with open("spin.in", "r") as f:
        for line in f:
            parts = list(map(int, line.strip().split()))
            speed = parts[0]
            wedge_count = parts[1]
            wedges = []
            for i in range(wedge_count):
                start = parts[2 + i * 2]
                extent = parts[3 + i * 2]
                wedges.append((start, extent))
            wheels.append((speed, wedges))
    return wheels

def get_open_angles(speed, wedges, time):
    open_angles = [False] * 360
    for start, extent in wedges:
        rotated_start = (start + speed * time) % 360
        for i in range(extent + 1):  # inclusive extent
            angle = (rotated_start + i) % 360
            open_angles[angle] = True
    return open_angles

def find_alignment_time(wheels):
    for t in range(360):  # simulate up to 360 seconds
        all_open = [True] * 360
        for speed, wedges in wheels:
            current_open = get_open_angles(speed, wedges, t)
            for i in range(360):
                all_open[i] = all_open[i] and current_open[i]
        for i in range(360):
            if all_open[i]:
                return t
    return None

def write_output(result):
    with open("spin.out", "w") as f:
        if result is None:
            f.write("none\n")
        else:
            f.write(str(result) + "\n")

def main():
    wheels = read_input()
    result = find_alignment_time(wheels)
    write_output(result)

main()