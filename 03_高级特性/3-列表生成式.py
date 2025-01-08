'''
列表生成式
- 是Python内置的非常简单却强大的可以用来创建list的生成式。
    - 例如：要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))：
'''
# 如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一：循环
L = []
for x in range(1, 11): 
    L.append(x * x); 
print(L); 

# 方法二：列表生成式； 使用列表生成式最终生成的列表会返回一个新的列表
newList = [x * x for x in range(1, 11)]; 
print(newList); 

# for循环后面还可以加上if判断，筛选出仅偶数的平方
newListTwo = [x * x for x in range(1, 11) if x % 2 == 0]; 
print(newListTwo); # [4, 16, 36, 64, 100]

