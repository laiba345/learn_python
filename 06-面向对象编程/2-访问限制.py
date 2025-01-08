'''
访问限制
- 在Class内部，可以有属性和方法，而外部代码可以通过直接调用实例变量的方法来操作数据，
- 这样，就隐藏了内部的复杂逻辑。
'''
# 但是从1-类和实例.py 的定义来看，外部代码还是可以自由地修改一个实例的属性
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

newStudent = Student('hk', 99)
print(newStudent.score) # 99
newStudent.score = 88
print(newStudent.score) # 88

'''
想让内部属性不被外部属性访问
- 做法：在属性的名称前面加上两个下划线__ 
    - 在py中，实例的变量名如果以__开头，就变成了一个私有变量（private） 
    - 只有内部可以访问，外部不能访问
- 作用
    - 确保了外部代码不能随意修改对象内部的状态，通过访问限制的保护
'''
class BStudent(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

BNewStudent = BStudent('kk', 100)
# print(BNewStudent.score) # 访问不到，直接报错；
BNewStudent.score = 12
print(BNewStudent.score) # 12 还是可以修改？

'''
如果外部代码要获取name和score属性怎么办？
- 方法：给Student类增加get_name和get_score方法
'''
class CStudent(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

HKK = CStudent('kkk', 10000)
HKK.print_score() # kkk: 10000 直接调用该方法即可

'''
如果又要允许外部代码修改score怎么办呢？
- 可以再给Student类增加set_score方法
'''
class DStudent(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad error')

HKK = DStudent('HH', 89)
HKK.set_score(98) # 设置完成
HKK.print_score() # 调用打印的方式

'''
总结：
1. 通过__来设置静态属性
2. 通过在类中设置方法来访问类中属性
3. 通过在类中设置方法来修改类中属性
'''

