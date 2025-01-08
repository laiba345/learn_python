'''
类和实例
- 类是抽象的模板，比如Student类
- 实例是根据类创建出来的一个个具体的“对象”，每个对象都拥有相同的方法，但各自的数据可能不同
'''

# 1. 定义类是通过class关键字,括号内紧接着的object，表明该类从哪个类继承下来
class Student(object):
    pass

# 2. 创建实例（类似于方法调用）
bart = Student()
print(bart) # <__main__.Student object at 0x0000021ED0E71B80>

# 3. 可以自由地给实例变量绑定属性
bart.name = 'hk'
print(bart.name)

# 4. 类可以起到模板的作用，在创建实例的时候，可以把一些我们认为必须绑定的属性强制填上去似
'''
    注意点
    1. __init__方法第一个参数永远是self，表示创建的实例本身（表示创建的实例本身）
    2. 在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
    3. 有了__init__方法，创建实例的时候，必须传入与__init__方法匹配的参数
    4. 与普通函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数
'''
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

newStudent = Student('hkk', 18)
print(newStudent.score) # 18

'''
  数据封装（主要通过类的方法来进行数据封装的操作）
  - 上面类中，每个实例都拥有各自的name和score属性，我们可以通过函数来访问这些数据；
  - 由于本身就有这些数据，所以在访问的时候，可以直接在Student类的内部定义访问数据的函数，这样就把数据封装起来了
  - 即：类的方法
'''
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

BStudent = Student('kkk', 25) # 创建实例的时候可以通过直接传入参数来进行
BStudent.print_score()  # kkk: 25

'''
    从外部看Student类，就只需要知道，创建实例需要给出name和score，
    而如何打印，都是在Student类的内部定义的，
    这些数据和逻辑被“封装”起来了，调用很容易，但却不用知道内部实现的细节。
    
    封装的另一个好处是可以给Student类增加新的方法，比如get_grade
    - 而且增加的这个新的方法可以直接调用之前定义好的参数； 
'''
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    # 调用参数的时候最好在类内部定义方法来使用；
    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

CStudent = Student('HHK', 26)
print(CStudent.name, CStudent.get_grade()) # HHK C