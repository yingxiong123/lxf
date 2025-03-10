import time, functools


def metric(text=None):
    if callable(text):  # 说明没有传参数，text 实际是 fn
        fn = text
        text = ''  # 设置默认文本为空
        return _create_wrapper(fn, text)
    else:
        def decorator(fn):
            return _create_wrapper(fn, text)
        return decorator

def _create_wrapper(fn, text):
    """ 创建装饰器的内部逻辑 """
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = fn(*args, **kwargs)
        end_time = time.time()
        print('%s%s executed in %.4f ms' % (text + ': ' if text else '', fn.__name__, (end_time - start_time) * 1000))
        return result
    return wrapper
# 测试
@metric('text test')
def fast(x, y):
    time.sleep(0.0012)
    print('2')
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
