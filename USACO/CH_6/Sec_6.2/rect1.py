"""
ID: amolgur1
LANG: PYTHON3
TASK: rect1
"""
import sys

# Increase recursion depth for deep overlaps
sys.setrecursionlimit(2000)

def solve():
    # Read inputs
    try:
        with open('rect1.in', 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        return

    # Parse first line: A (width), B (height), N (count)
    first_line = list(map(int, lines[0].split()))
    A, B, N = first_line[0], first_line[1], first_line[2]

    # Store rectangles as (x1, y1, x2, y2, color)
    # Paper is the first rectangle (index 0), color 1
    rects = [(0, 0, A, B, 1)]

    # Parse subsequent N lines
    for i in range(N):
        # Input: llx, lly, urx, ury, color
        # Note: Input coordinates are essentially 0-indexed grid lines
        # rect defined by (llx, lly) to (urx, ury) covers the area exactly
        # width = urx - llx, height = ury - lly
        r = list(map(int, lines[i+1].split()))
        rects.append(tuple(r))

    # Dictionary to store total area for each color
    # Key: color, Value: area
    color_areas = {}

    # Recursive function to compute visible area of a rectangle `r`
    # considering occlusions by rectangles from index `start_idx` onwards
    def get_visible_area(x1, y1, x2, y2, start_idx):
        # If rectangle is degenerate (invalid), area is 0
        if x1 >= x2 or y1 >= y2:
            return 0
        
        # If no more rectangles on top, this entire piece is visible
        if start_idx >= len(rects):
            return (x2 - x1) * (y2 - y1)
        
        # Rectangle that might cover the current one
        cx1, cy1, cx2, cy2, _ = rects[start_idx]

        # Check for intersection
        # If no overlap, simply check against the next rectangle
        if x2 <= cx1 or x1 >= cx2 or y2 <= cy1 or y1 >= cy2:
            return get_visible_area(x1, y1, x2, y2, start_idx + 1)

        # If there is an overlap, we split the current rectangle (x1,y1,x2,y2)
        # into pieces that are NOT covered by (cx1,cy1,cx2,cy2)
        
        total_area = 0
        
        # 1. Left piece
        if x1 < cx1:
            total_area += get_visible_area(x1, y1, cx1, y2, start_idx + 1)
            x1 = cx1 # Crop current rect to remove the left part processed
            
        # 2. Right piece
        if x2 > cx2:
            total_area += get_visible_area(cx2, y1, x2, y2, start_idx + 1)
            x2 = cx2 # Crop current rect
            
        # 3. Bottom piece
        if y1 < cy1:
            total_area += get_visible_area(x1, y1, x2, cy1, start_idx + 1)
            y1 = cy1 # Crop current rect
            
        # 4. Top piece
        if y2 > cy2:
            total_area += get_visible_area(x1, cy2, x2, y2, start_idx + 1)
            # No need to update y2, as this is the last split logic
            
        # The remaining center part (if valid) is fully covered by the covering rect,
        # so we do not add its area.
        
        return total_area

    # Initialize areas for known colors (from 1 to 2500 max possible)
    # Optimization: Only track colors we actually encounter
    for r in rects:
        color_areas[r[4]] = 0

    # Calculate visible area for each rectangle
    # We iterate through all rectangles (including the base paper)
    # and calculate how much of *that specific rectangle* remains visible.
    for i in range(len(rects)):
        x1, y1, x2, y2, color = rects[i]
        # Check against all subsequent rectangles
        visible = get_visible_area(x1, y1, x2, y2, i + 1)
        color_areas[color] += visible

    # Write output sorted by color
    sorted_colors = sorted(color_areas.keys())
    with open('rect1.out', 'w') as f:
        for c in sorted_colors:
            area = color_areas[c]
            if area > 0:
                f.write(f"{c} {area}\n")

if __name__ == "__main__":
    solve()