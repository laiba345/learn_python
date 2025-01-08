'''
实例属性和类属性
'''

'''
实例属性和类属性
- Python是动态语言，根据类创建的实例可以任意绑定属性
- 给实例绑定属性的方法是通过实例变量，或通过self变量
    - 给实例绑定属性的方法是通过实例变量，
'''
class Student(object):
    def __init__(self, name):
        self.name = name

s1 = Student('kk')
s1.score = 99

