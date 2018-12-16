'''
You will be given an array a and a value x. All you need to do is check whether the provided array contains the value.

Array can contain numbers or strings. X can be either.

Return true if the array contains the value, false if not.
'''


def check(seq, elem):
    y = 0
    for x in seq:
        if x == elem:
            y += 1
            break
    if y == 1:
        return True
    else:
        return False
