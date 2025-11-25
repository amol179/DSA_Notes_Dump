"""
ID: amolgur1
LANG: PYTHON3
TASK: calfflac
"""
import sys

def solve():
    # Read the entire input at once
    try:
        with open('calfflac.in', 'r') as f:
            original_text = f.read()
    except FileNotFoundError:
        return

    # Preprocessing:
    # 1. Create a clean string (only letters, lowercase)
    # 2. Create a map from clean_index -> original_index
    clean_text = []
    index_map = []
    
    for i, char in enumerate(original_text):
        if char.isalpha():
            clean_text.append(char.lower())
            index_map.append(i)
            
    # Convert list to string for easier handling
    clean_str = "".join(clean_text)
    n = len(clean_str)
    
    max_len = 0
    best_start = 0 # Index in clean_str
    best_end = 0   # Index in clean_str

    # Helper to update maximum found
    def update_max(start, end):
        nonlocal max_len, best_start, best_end
        # Length is end - start + 1
        current_len = end - start + 1
        if current_len > max_len:
            max_len = current_len
            best_start = start
            best_end = end

    # Iterate through all possible centers
    for i in range(n):
        # 1. Odd length palindromes (centered at i)
        left, right = i, i
        # Constraint optimization: Max palindrome is 2000, radius 1000
        # We stop if we hit boundaries or mismatch
        while left >= 0 and right < n and clean_str[left] == clean_str[right]:
            if (right - left + 1) > 2000: break 
            left -= 1
            right += 1
        # Step back to last valid position
        update_max(left + 1, right - 1)

        # 2. Even length palindromes (centered between i and i+1)
        left, right = i, i + 1
        while left >= 0 and right < n and clean_str[left] == clean_str[right]:
            if (right - left + 1) > 2000: break 
            left -= 1
            right += 1
        update_max(left + 1, right - 1)

    # Map back to original coordinates
    # If no palindrome found (rare edge case with 0 letters), handle gracefully
    if max_len == 0:
        final_output = ""
        final_len = 0
    else:
        orig_start_index = index_map[best_start]
        orig_end_index = index_map[best_end]
        final_output = original_text[orig_start_index : orig_end_index + 1]
        final_len = max_len

    # Output
    with open('calfflac.out', 'w') as f:
        f.write(f"{final_len}\n")
        f.write(f"{final_output}\n")

if __name__ == "__main__":
    solve()