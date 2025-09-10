"""
ID: amolgur1
LANG: PYTHON3
TASK: job
"""

# job.py

def main():
    fin = open("job.in", "r")
    fout = open("job.out", "w")

    # Read input
    first_line = fin.readline().strip().split()
    N, M1, M2 = map(int, first_line)
    times = []
    while len(times) < M1 + M2:
        times += list(map(int, fin.readline().strip().split()))

    A_times = times[:M1]
    B_times = times[M1:]

    # --- Phase A: schedule jobs on A-machines ---
    A_finish = [0] * N
    machine_finish_A = [0] * M1

    for j in range(N):
        best_machine = 0
        best_finish = machine_finish_A[0] + A_times[0]
        for i in range(1, M1):
            finish_time = machine_finish_A[i] + A_times[i]
            if finish_time < best_finish:
                best_finish = finish_time
                best_machine = i
        machine_finish_A[best_machine] = best_finish
        A_finish[j] = best_finish

    A_finish.sort()
    min_A = A_finish[-1]  # all A completed

    # --- Phase B: schedule jobs independently (like A, but for N jobs) ---
    B_complete = [0] * N
    machine_finish_B = [0] * M2

    for j in range(N):
        best_machine = 0
        best_finish = machine_finish_B[0] + B_times[0]
        for i in range(1, M2):
            finish_time = machine_finish_B[i] + B_times[i]
            if finish_time < best_finish:
                best_finish = finish_time
                best_machine = i
        machine_finish_B[best_machine] = best_finish
        B_complete[j] = best_finish

    B_complete.sort()

    # --- Combine A and B times ---
    min_B = 0
    for i in range(N):
        # Pair largest A with smallest B
        finish_time = A_finish[i] + B_complete[N - 1 - i]
        if finish_time > min_B:
            min_B = finish_time

    # Output result
    fout.write(str(min_A) + " " + str(min_B) + "\n")

    fin.close()
    fout.close()


if __name__ == "__main__":
    main()
