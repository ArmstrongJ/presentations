from math import factorial

def exp_right(x):
    ret = 1
    negative = (x < 0)

    xa = abs(x)

    for i in range(1, 128):
        ret = ret + xa**float(i) / float(factorial(i))

    if negative:
        ret = 1.0/ret

    return ret

def exp_wrong(x):
    ret = 1

    for i in range(1, 128):
        ret = ret + x**float(i) / float(factorial(i))

    return ret
