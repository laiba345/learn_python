'''
继承和多态
'''

'''
OPP程序设计
- 定义一个class的时候，可以从某个现有的class继承，新的class称为子类（Subclass）
- 被继承的class称为基类、父类或超类
'''
# 定义一个名为Animal的class类
class Aniaml(object):
    def run(self):
        print('Animal is running...')

# 编写Dog和Cat类的时候，就可以直接从Animal继承
class ADog(Aniaml):
    def run(self):
        print('Dog is running')

class ACat(Aniaml):
    def run(self):
        print('Cat is running')

'''
继承的好处
- 最大的好处是子类获得了父类的全部功能
- 由于Animal实现了run()方法，因此，Dog和Cat作为它的子类，什么事也没干，就自动拥有了run()方法：
- 当子类和父类都存在相同的方法时，子类会覆盖父类方法； 
'''
dog = ADog()
dog.run()  # Dog is running

'''
多态
- 当我们定义一个class的时候，我们实际上定义了一种数据类型
- 我们定义的数据类型和Python自带的数据类型，比如str、list、dict没什么两样
'''
a = list() # a是list类型
b = Aniaml() # b是Animal类型
c = ADog() # c是Dog类型

# 判断一个变量是否是某个类型可以使用isinstance判断；
print(isinstance(a, list)) # True

'''
但是注意
- c不仅仅是Dog还是Aniaml类型； 
- 所以：在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类。但是，反过来就不行：
'''
print(isinstance(c, Aniaml)) # True

'''
理解多态的好处：
- 编写一个函数,该函数可以接受一个Animal类型的变量
- 通过下面可以发现
    - 新增一个Animal的子类，不必对run_twice()做任何修改，
    - 实际上，任何依赖Animal作为参数的函数或者方法都可以不加修改地正常运行，原因就在于多态。
- 多态的好处
    - 当我们需要传入Dog、Cat、Tortoise……时，我们只需要接收Animal类型就可以了
    - 按照Animal类型进行操作即可，
    - 由于Animal类型有run()方法，因此，传入的任意类型，只要是Animal类或者子类，就会自动调用实际类型的run()方法
    - 对于一个变量，我们只需要知道它是Animal类型，无需确切地知道它的子类型，就可以放心地调用run()方法，而具体调用的run()方法是作用在Animal、Dog、Cat还是Tortoise对象上，由运行时该对象的确切类型决定，这就是多态真正的威力：
    - 调节方只管调节，不管细节，而当我们新增一种Animal的子类时，只要确保run()方法编写正确，不用管原来的代码是如何调用的
'''
def run_twice(animal):
    animal.run()
    animal.run()

print(run_twice(Aniaml()))
print(run_twice(ADog()))

'''
静态语言 VS 动态语言
- 对于静态语言（例如Java），如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。
- 对于动态语言（例如Python） 则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了：
- 真的能进行调用（#83）
    - 这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。
'''
class Timer(object):
    def run(self):
        print('Start')

print(run_twice(Timer()))  # 还真的能调用



