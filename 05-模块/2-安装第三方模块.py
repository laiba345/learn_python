'''
在Python中，安装第三方模块，是通过包管理工具pip完成的。
- 面向对象最重要的概念就是类和实例，必须牢记类是抽象的模板，比如Student类，
- 而实例是根据类创建出来的一个个具体的“对象”，每个对象都拥有相同的方法，但各自的数据可能不同。
'''
# 定义类是通过class关键字
class Student(object): 
    pass

bart = Student()
print(bart)
print(Student)

bart.name = 'hk'
print(bart.name); 

# 由于类可以起到模板的作用，因此在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去
# 通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score属性绑定上去
