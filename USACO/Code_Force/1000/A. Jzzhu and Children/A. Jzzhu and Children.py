from collections import deque


def last_child(n, m, candies):
    # Create a queue with tuples (child_index, candies_needed)
    queue = deque((i + 1, candies[i]) for i in range(n))

    last_child = 0

    while queue:
        child, candies_needed = queue.popleft()  # Take the first child from the line
        if candies_needed > m:
            # If the child still needs more candies, put them at the end of the line
            queue.append((child, candies_needed - m))
        else:
            # If the child's requirement is fulfilled, this is the last child to leave so far
            last_child = child

    return last_child


# Taking custom input
n, m = map(int, input().split())
candies = list(map(int, input().split()))

# Calling the function and displaying the result
print(last_child(n, m, candies))
