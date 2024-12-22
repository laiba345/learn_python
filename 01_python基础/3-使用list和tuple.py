# list（列表）可以随时添加删除元素
classmates = ['fl', 'hk', 'kk']; 
print(classmates); 
print(len(classmates)); 
# 访问元素
print(classmates[0]); 
print(classmates[-1]); # 'kk'（倒数第一个）

# append 添加元素
classmates.append('Adam'); 
print(classmates); 
# pop 删除元素
print(classmates.pop()); # Adam (使用pop方法单独返回被删除的元素)

# 赋值 替换元素
classmates[1] = 'hyl'; 
print(classmates); 

'''
重要观点
1. List里面的元素的数据类型也可以不同
- L = ['Apple', 123, True]
2. List数组中可以有另外一个数组
- s = ['python', 'java', ['asp', 'php'], 'scheme']
'''

'''
tuple
- 元组（有序列表）, tuple和list非常类似，但是tuple初始化以后就不能修改了； 
- 区别
    - 因为不能变了，所以其没有append(), insert()方法
    - 利用索引获取元素还是没问题的
    - 因为不可变，所以更安全
- 注意1
    - 当只有一个元素的tuple定义时，必须加一个逗号, 来消除歧义
    - t = (1, )
- 注意2
    - tuple一开始指向的list并没有改成别的list，
    - 所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。
    - 即指向'a'，就不能改成指向'b'，指向一个list，
    - 就不能改成指向其他对象，但指向的这个list本身是可变的！
'''
classmatesTwo = ('Michael', 'Bob', 'Tracy')
print(classmatesTwo); 