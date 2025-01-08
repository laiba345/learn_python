'''
可以直接作用于for循环的数据类型称为：Iterable
- 1. 集合数据类型：list、tuple、dict、set、str
- 2. generator； 
    - 生成器
    - 带yield的generator function
'''
# 1. 可以使用isinstance() 判断一个对象是否是可迭代对象Iterable对象
from collections.abc import Iterable
print(isinstance([], Iterable)); # True

'''
2. 生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，
直到最后抛出StopIteration错误表示无法继续返回下一个值了。

注意：可以被next函数调用并不断返回下一个值的对象称为迭代器：Iterator
同样可以使用isinstance() 判断一个对象是否是可迭代对象Iterator对象
'''
from collections.abc import Iterator
print(isinstance([], Iterator)); # False

# Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
# 要把list、dict、str等Iterable变成Iterator可以使用iter()函数：
print(isinstance(iter([]), Iterator)); # True