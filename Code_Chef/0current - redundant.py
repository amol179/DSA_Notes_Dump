def find_min_cost_operations(array):
    total_cost = 0
    operations = []
    target_value = min(array)  # Target value to transform the array to the minimum element

    # Iterate over the array and find ranges to minimize
    i = 0
    while i < len(array):
        if array[i] != target_value:
            L = i + 1
            while i < len(array) and array[i] != target_value:
                i += 1
            R = i
            x = target_value
            cost = (R - L + 1) * x
            
            # Apply the operation to the array
            for j in range(L - 1, R):
                array[j] = x
            
            operations.append((L, R, x))
            total_cost += cost
        i += 1

    return array, total_cost, operations

# Initial array
array = [1, 3, 1, 4, 3, 4, 3]

# Find the optimal operations
final_array, total_cost, operations = find_min_cost_operations(array)

print("Final array:", final_array)
print("Total cost:", total_cost)
print("Operations (L, R, x):", operations)
