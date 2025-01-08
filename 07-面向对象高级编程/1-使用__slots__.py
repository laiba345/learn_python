class Student(object):
    pass

# 尝试给实例绑定一个属性
s = Student()
s.name = 'kk'
print(s.name) # kk

# 尝试给实例绑定一个方法
def set_age(self, age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s)

'''
如果我们想要限制实例的属性怎么办？
- 比如：只允许对Student实例添加name和age属性； 
- 注意
    - __slots__定义的属性仅对当前实例起作用
    - 对继承的子类是不起作用的；
'''
class Student1(object):
    __slots__ = ('name', 'age') # 需要注意的是：关键字是slots

s1 = Student1()
s1.name = 'kk'
print(s1.name) # 'kk'

s1.score = 99
print(s1.score) # 报错