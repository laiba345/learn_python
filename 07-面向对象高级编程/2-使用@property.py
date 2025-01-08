'''
装饰器
'''

'''
装饰器（decorator）
- 装饰器可以给函数动态加上功能；
- 对于类方法，装饰器一样起作用；
- Python内置的@property装饰器就是负责把一个方法变成属性调用的：
'''
class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100')
        self._score = value

'''
把一个getter方法变成属性，只需要加上@property就可以了
此时，@property本身又创建出了另一个装饰器 @score.setter
负责把一个setter方法变成属性赋值，这样我们就拥有一个可控的属性操作；
'''
s = Student()
s.score = 60
print(s.score) # 60

'''
注意到这个神奇的@property
- 我们在对实例属性操作的时候，就知道该属性很可能不是直接暴露的，
- 而是通过getter和setter方法来实现的；
'''
