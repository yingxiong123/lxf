from functools import reduce


DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char2num(s):
    return DIGITS[s]

def fn(x,y):
    return 10*x+y

def str2float(s):
    a = s.split('.')
    letf =  reduce(fn,map(char2num,a[0]))
    right = reduce(fn,map(char2num,a[1]))
    return  letf+ right*(10**(-len(a[1])))

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
