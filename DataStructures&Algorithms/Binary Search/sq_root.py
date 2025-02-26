# Problem  from - https://www.youtube.com/shorts/vuj9OnJaHnE

# pritty simple application of the Binary search
#


def mySq(x):
    # L is the initial length
    # R is the n'th of the length
    L, R = 1, x
    while L <= R:
        # initial and final length is used to find the exact mid
        M = (L + R) // 2
        M_sq = M * M

        # Compare with the mid value squared
        if M_sq == x:
            return M
        elif M_sq < x:
            L = M + 1
        else:
            R = M - 1
    return R


print(mySq(x=int(input())))
