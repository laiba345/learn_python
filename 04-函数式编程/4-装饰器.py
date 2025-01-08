'''
装饰器
- 函数是一个对象，而且函数对象可以被赋值给变量，所以通过变量也可以调用该函数
'''
# 通过变量调用函数示例：
def now():
    print('2024-6-1')
f = now
f() # 2024-6-1

# 函数对象中有__name__属性，可以拿到函数名字
print(now.__name__);  # now
print(f.__name__); # now

'''
现在，假设我们要增强now()函数的功能
- 1. 在函数调用前后自动打印日志，但是不希望修改now()函数定义
- 2. 这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
- 3. 本质上，Decorator就是一个返回函数的高阶函数；
'''
# 定义一个能打印日志的Decorator，可以定义如下
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

# 上述log函数，可以接收一个函数作为参数，并返回一个函数
# 借助Python的@语法，把decorator置于函数的定义处：
@log
def now():
    print('2024-6-1')

now(); # call now(): 2024-6-1

# 注意：把@log放到now()函数的定义处，相当于执行了语句：now = log(now)