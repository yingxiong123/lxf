from functools import reduce

def fn(x,y):
    return x * 10+y

print(reduce(fn, [1, 2, 3, 7]))

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char2num(s):
    return DIGITS[s]

def str2int(s):
    return reduce(fn, map(char2num, s))

def str2int(s):
    return reduce(lambda x, y: x*10+y, map(char2num, s))

s = '2446661'
print(list(map(char2num, s)))
print(str2int(s))