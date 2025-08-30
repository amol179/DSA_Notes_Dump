"""
ID: amolgur1
LANG: PYTHON3
TASK:  heritage
"""

def build_post_order(in_order, pre_order):
    if not in_order:
        return ""
    
    root = pre_order[0]
    root_index = in_order.index(root)
    
    left_in = in_order[:root_index]
    right_in = in_order[root_index + 1:]
    
    left_pre = pre_order[1:1 + len(left_in)]
    right_pre = pre_order[1 + len(left_in):]
    
    left_post = build_post_order(left_in, left_pre)
    right_post = build_post_order(right_in, right_pre)
    
    return left_post + right_post + root

# Read input from file
with open("heritage.in", "r") as fin:
    in_order = fin.readline().strip()
    pre_order = fin.readline().strip()

# Generate post-order traversal
post_order = build_post_order(in_order, pre_order)

# Write output to file
with open("heritage.out", "w") as fout:
    fout.write(post_order + "\n")