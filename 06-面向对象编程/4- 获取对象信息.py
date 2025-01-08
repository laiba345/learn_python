'''
获取对象信息
'''

'''
获取对象信息
- 我们使用type()函数来判断对象类型
- 如果一个变量指向函数或类，也可以使用type() 判断； 
'''
print(type(123)) # <class 'int'>
print(type('str'))
print(type(abs)) # <class 'builtin_function_or_method'>

'''
判断一个对象是否是函数？
- 可以使用types模版中定义的常量
'''
import  types
def fn():
    pass
# print(type(fn) === types.FunctionType)

'''
对于class的继承关系来说，要判断class类型，可以使用isinstance() 函数
- 之间的继承关系；object -> Animal -> Dog -> Husky
- isinstance()就可以告诉我们，一个对象是否是某种类型。
- 用法：isinstance(h, Dog)
- 提示：总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。
'''

'''
dir() 函数
- 如果要获取一个对象的所有属性和方法，可以使用dir() 方法，
- 其返回一个包含字符串的list，比如获得一个str对象的所有属性和方法； 
- 类似于__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__返回长度； 
'''
print(dir('ABC')) # 一个数组，里面包含
'''
总结：通过内置的一系列函数，我们可以对任意一个Python对象进行解析；
- 获取任意一个python对象的属性和方法； 
'''
