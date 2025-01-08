'''
匿名函数
- 有些时候在传入函数时，不需要显式地定义函数，直接传入匿名函数更方便
- lambda x: x * x
    - 关键字lambda 表示匿名函数，冒号前面的x表示函数参数
    - 匿名函数只能有一个表达式，不用写return 
'''
print(list(map(lambda x: x * x, [1, 2, 3, 4]))); # [1, 4, 9, 16]

# 也可以把匿名函数作为返回值返回，例如
def build(x, y):
    return lambda: x * x + y * y