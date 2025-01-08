'''
生成器
- 在py中，一边循环一边计算的机制，称为生成器generator
- 创建generator的方法
    - 1. 将列表生成式的[] 改为 {}
'''
# 方法1
L = (x * x for x in range(10))
print(L) # <generator object <genexpr> at 0x000002220960E260>

# 要打印出内容的话，需要使用next()函数
print(next(L)); # 0
print(next(L)); # 1
print(next(L)); # 4

# 方法2 定义某个函数，使用yield来返回内容
def odd(): 
    print('step1'); 
    yield 1;   
    print('step2'); 
    yield 2;   

# 在调用该generator函数时，首先要生成一个generator对象，然后用next()函数不断获得下一个返回值：
# 即yield前面的内容都可以直接返回；
o = odd(); 
print(next(o)); # step1 1 