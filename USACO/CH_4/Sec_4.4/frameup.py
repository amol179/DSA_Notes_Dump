"""
ID: amolgur1
LANG: PYTHON3
TASK:  frameup
"""


import sys

def solve():
    """
    Main function to solve the frame-up problem.
    """
    # Read input from 'frameup.in'
    with open('frameup.in', 'r') as f:
        H, W = map(int, f.readline().split())
        grid = [f.readline().strip() for _ in range(H)]

    # 1. Identify all unique frames (letters) and find their bounding boxes.
    frames = {}
    for r in range(H):
        for c in range(W):
            char = grid[r][c]
            if 'A' <= char <= 'Z':
                if char not in frames:
                    frames[char] = {'min_r': r, 'max_r': r, 'min_c': c, 'max_c': c}
                else:
                    frames[char]['min_r'] = min(frames[char]['min_r'], r)
                    frames[char]['max_r'] = max(frames[char]['max_r'], r)
                    frames[char]['min_c'] = min(frames[char]['min_c'], c)
                    frames[char]['max_c'] = max(frames[char]['max_c'], c)
    
    letters = sorted(frames.keys())
    num_letters = len(letters)

    # 2. Build the dependency graph.
    # An edge from U -> V means U is underneath V.
    graph = {l: set() for l in letters}
    in_degree = {l: 0 for l in letters}

    for letter, bounds in frames.items():
        min_r, max_r = bounds['min_r'], bounds['max_r']
        min_c, max_c = bounds['min_c'], bounds['max_c']
        
        # Check all cells on the border of the bounding box
        border_cells = set()
        for c in range(min_c, max_c + 1):
            border_cells.add((min_r, c))
            border_cells.add((max_r, c))
        for r in range(min_r, max_r + 1):
            border_cells.add((r, min_c))
            border_cells.add((r, max_c))

        for r, c in border_cells:
            char_on_top = grid[r][c]
            if 'A' <= char_on_top <= 'Z' and char_on_top != letter:
                # 'char_on_top' covers 'letter'. Add dependency.
                if char_on_top not in graph[letter]:
                    graph[letter].add(char_on_top)
                    in_degree[char_on_top] += 1
    
    # 3. Find all topological sorts using recursive backtracking.
    results = []
    
    def find_all_topological_sorts(path, current_in_degree):
        if len(path) == num_letters:
            results.append("".join(path))
            return

        # Find all nodes with an in-degree of 0
        candidates = []
        for l in letters:
            if current_in_degree[l] == 0 and l not in path:
                candidates.append(l)
        
        # Process candidates in alphabetical order to get sorted output
        candidates.sort()

        for node in candidates:
            # Recurse with the new state
            new_path = path + [node]
            new_in_degree = current_in_degree.copy()
            for neighbor in graph[node]:
                new_in_degree[neighbor] -= 1
            
            find_all_topological_sorts(new_path, new_in_degree)

    find_all_topological_sorts([], in_degree)
    
    # Write results to 'frameup.out'
    with open('frameup.out', 'w') as f:
        for res in sorted(results): # Final sort just in case, but recursion order should handle it
            f.write(res + '\n')

if __name__ == "__main__":
    solve()
