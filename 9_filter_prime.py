
'''
    这个函数用来求解1000以内的素数,采用filter函数
'''

#用来取出所有的奇数,生成器3，5，7，9
def _odd():
    n = 1
    while True:
        n = n+2
        yield n

def primes():
    yield 2
    it = _odd()  #生成器也是Iterable
    while True:
        n = next(it)  #第一个it是3
        yield n
        it = filter(lambda x : x % n > 0, it)

# 打印1000以内的素数:
for n in primes():
    if n < 100:
        print(n)
    else:
        break






