def min_time(n, tasks):
    current_position = 1
    total_time = 0

    for task in tasks:
        if task >= current_position:
            total_time += task - current_position
        else:
            total_time += n - current_position + task
        current_position = task

    return total_time


n, m = map(int, input().split())
tasks = list(map(int, input().split()))

print(min_time(n, tasks))
