'''
对经常取指定索引范围的操作，使用切片操作符，极大简化
'''
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']; 
# L[x:y]; 索引从x开始到y-1
print(L[0:3]); # ['Michael', 'Sarah', 'Tracy'] 
# 切片可以轻松取出某一段数列；比如前10个数字 L[:10], 后10个数字L[-10:]
# 前10个数，每两个取一个L[:10:2]
# 每5个取1个；L[::5]
# 什么都不写，只写[:]可以同样复制一个list
