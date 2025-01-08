'''
给定一个list或tuple，可以通过for循环来遍历它们，这种遍历就称之为迭代
py中，使用for...in来完成
py中的for循环不仅可以用在list或tuple上，还可以用在其他可迭代对象上
    - 只要是可迭代对象，无论有无下标，都可以迭代，比如dict就可以迭代：
'''
d = { 'a': 1, 'b': 2, 'c': 3 }; 
for key in d: 
    print(key); # 因为dict的存储不是按照list的方式顺序排列，所以迭代出的结果很可能不一样

# 如果想要迭代value，可以用for value in d.values()
# 如果要同时迭代key和value，可以用for k,v in d.items() 
for k, v in d.items():
    print(k, v); 

# 如何判断一个对象是不是可迭代对象呢？通过collections.abc模块的Iterable类型判断
from collections.abc import Iterable; 
print(isinstance('abc', Iterable)); # True

'''
如果要对list实现类似java那样的下表循环怎么搞
- enumerate函数可以把一个list变成索引-元素对
'''
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)