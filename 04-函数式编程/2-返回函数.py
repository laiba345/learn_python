# 通常情况下，求和函数的定义
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

# 但是如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？可以不返回求和的结果，而是返回求和的函数：
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

# 调用lazy_sum() 时，返回的并不是求和结果，而是求和函数
f = lazy_sum(1, 3, 5, 7, 9); 
print(f); # <function lazy_sum.<locals>.sum at 0x0000016EA8F8D260>

# 调用函数f时，才真正计算求和的结果
print(f()); # 25 

