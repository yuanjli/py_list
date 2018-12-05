# Given a 32-bit signed integer, reverse digits of an integer.

def reverse(x):

    result = 0
    # handle the negative case:
    if x < 0:
        neg = -1
        x = -x
    else:
        neg = 1

    while x != 0:
        result = result * 10 + x % 10
        x /= 10
        # if the the result overflow the integer range: [−231,  231 − 1], return 0
        if result > 2147483647 or result < -2147483648:
            return 0
    return result * neg


