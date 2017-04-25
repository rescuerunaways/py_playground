# compute parity
# how do we compute parity of a very large number of 64 bit words?
#
import numpy


def parity_str(x):
    s = 0
    for i in x:
        if i == '1':
            s += 1
    if s % 2 == 0:
        return 'even'
    else:
        return 'odd'


def parity_int(x):
    s = 0
    while x != 0:
        # if the right this(which is about to be pushed away), was 1, count it  :)
        s ^= (x & 1)
        # pushes away the right thing
        x = numpy.right_shift(x, 1)
    return s


def parity_optimized(x):
    s = 0
    while x != 0:
        # if it was a bit, count it :)
        s = s ^ 1
        # clears lowest (right-most bit)
        x = x & (x - 1)
    return s


print(parity_str('1100011'))
print(parity_int(0b11000110))
print(parity_optimized(0b011000110))
