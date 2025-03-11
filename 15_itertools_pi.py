import itertools

def pi(N):
    ' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    odds = itertools.islice(itertools.count(1, 2), N)  # 取前N项
    
    # step 2: 计算莱布尼茨级数
    terms = [(4 / x) * (-1) ** (i + 1) for i, x in enumerate(odds, start=1)]
    
    # step 3: 求和
    return sum(terms)

# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))

assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415

print('ok')
