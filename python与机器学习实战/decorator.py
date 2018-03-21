import time
import wrapt


def decorator(eps):
    @wrapt.decorator
    def wrapper(func, instance, args, kwargs):
        t = time.time()
        ans = func(*args, **kwargs)
        t = time.time() - t
        if t > eps:
            print('Slow!')
        else:
            print('Fast!')
        return ans, t

    return wrapper


@decorator(0.01)
def func1():
    for _ in range(10 ** 6):
        x = 0
    return 'Done'


@decorator(0.05)
def fun2():
    for _ in range(10 ** 6):
        x = 0
    return 'Done'


print(func1())  # 将会输出两行。第一行为‘Slow！’，第二行为（‘Done’，0.02810549736）
print(fun2())  # 将会输出两行。第一行为‘Fast！！’，第二行为（‘Done’，0.02810549736）
