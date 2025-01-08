# 计算x的n次方
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(2, 5)); # 32 

# 默认参数（在函数中写死了某个参数）
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

# 可变参数
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc([1, 2, 3])); # 14

# 使用* 号来表示可变参数的形式
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
# 由于变成了可变参数，所以在调用该函数的时候可以传入任意个参数
print(calc(1, 2)); # 5 