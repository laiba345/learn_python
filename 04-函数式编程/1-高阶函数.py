'''
高阶函数
- map和reduce函数
    - map函数接受两个参数
        - 一个是函数，另一个是Iterable
        - map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
'''
def f(x):
    return x * x; 

r = map(f, [1, 2, 3, 4]); # 也可以合并成为一行
print(list(r)); # [1, 4, 9, 16]

'''
reduce的用法
- reduce把一个函数作用在一个序列[x1, x2, x3,...]
- 这个函数必须接收两个参数，
- reduce把结果继续和序列的下一个元素做累积计算

# reduce的效果等同于
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
'''
# 实现1；对一个序列求和，可以使用reduce实现；可以用内建函数sum() 
from functools import reduce
def add(x, y):
    return x + y
print(reduce(add, [1, 3, 5, 7, 9]));  # 25

# 实现2；把序列[1, 3, 5, 7, 9]变换成整数13579， 
def fn(x, y):
    return x * 10 + y; 
print(reduce(fn, [1, 3, 5, 7, 9])); # 13579

'''
filter()函数
- 用于过滤序列
- 用法
    - 也接收一个函数和一个序列
    - filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定是否保留元素
'''
def is_odd(n):
    return n % 2 == 1

print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))); # [1, 5, 9, 15]

'''
sorted函数
- Python内置的sorted()函数就可以对list进行排序：
'''
print(sorted([36, 5, -12, 9, -21])); # [-21, -12, 5, 9, 36]