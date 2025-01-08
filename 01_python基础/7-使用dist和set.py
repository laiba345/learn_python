'''
字典dict, 在java中称为map，使用键值对(key-value)来存储，具有极快的查找速度； 
- 用处； 假设要根据同学的名字查找对应的成绩，
- 为什么dict查找速度这么快？
    - 理解原理，类似于查字典一样； 
- 理解
    - 1. 一个key只能对应一个value，所以多次对key放入value，后面的值会把前面的值替换
    - 2. 判断key是否存在
        - in
        - get()方法
    - 3. 要删除一个key，使用pop(key)方法，对应的value也会被删除
    - 4. 注意：dict内部存放的顺序和key放入的顺序是没有关系的。
- 与list相比，dict特点
    - 查找和插入的速度极快，不会随着key的增加而变慢；
    - 需要占用大量内存，内存浪费过多；
    - dict是一种使用 空间来换时间的方法；
- dict可以用在需要高速查找的地方，
    - dict的key必须是不可变对象；
'''
import sys; 
# 确保输出使用 UTF-8 编码
sys.stdout.reconfigure(encoding='utf-8')

scores = { 'hk': 99, 'hkk': 88, 'lyf': 66}
print('hk的分数是', scores['hk'])
print('hk' in scores) # True
print(scores.get('kkkk')) # None


'''
set
- 和dict类似，也是一组key的集合，但是不存储value，
    - 重复的元素在set集合中会被过滤掉； 
'''
s = { 1, 1, 2, 3, 4, 5, 6, 5}
print(s) # {1, 2, 3, 4, 5, 6}
# 通过add(key)方法，可以添加元素到set中
s.add(9)
print(s)
# 通过remove(key)方法，可以删除元素
s.remove(9)
print(s)

'''
谈区别
- 唯一的区别在于是set没有存储对应的value
- 同样的，不可以放入可变对象（list列表）
    - 可变对象list，其内部的内容是会变化的；
'''