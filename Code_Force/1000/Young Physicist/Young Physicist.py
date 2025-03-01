def is_in_equilibrium(forces):
    # Initialize sums for x, y, and z coordinates
    sum_x = 0
    sum_y = 0
    sum_z = 0

    # Sum up the coordinates of all forces
    for force in forces:
        sum_x += force[0]
        sum_y += force[1]
        sum_z += force[2]

    # Check if all sums are zero
    if sum_x == 0 and sum_y == 0 and sum_z == 0:
        return "YES"
    else:
        return "NO"


# Read input
n = int(input())
forces = [list(map(int, input().split())) for _ in range(n)]

# Determine if the body is in equilibrium
result = is_in_equilibrium(forces)
print(result)
