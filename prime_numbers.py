from functools import reduce

def f1(s):
    return filter(lambda x: x % s[0], s)
def f2(res, numbers):
    return res + [numbers[0]]


my_list = range(2, 20)
