'''
偏函数
- 通过固定函数的一部分参数来创建新的函数的技术
- 偏函数由functions模块中的partial函数提供，
- 目的是让某些参数固定后产生一个新的函数，这个新函数可以像普通函数一样使用。
- 其实用的也很少，没啥用
'''
from functools import partial

def multiply(x, y):
    return x * y
# 创建一个偏函数
double = partial(multiply, y = 10)
print(double(5)); # 50 