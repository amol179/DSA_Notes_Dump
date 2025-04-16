def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return (a * b) // gcd(a, b)


def find_string_lcm(s, t):
    len_s, len_t = len(s), len(t)
    lcm_length = lcm(len_s, len_t)  # Compute LCM manually without using `math` module

    s_expanded = s * (lcm_length // len_s)
    t_expanded = t * (lcm_length // len_t)

    return s_expanded if s_expanded == t_expanded else "-1"


# Reading input
q = int(input())
for _ in range(q):
    s = input().strip()
    t = input().strip()
    print(find_string_lcm(s, t))
