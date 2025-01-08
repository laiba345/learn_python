'''
错误处理
'''

'''
使用try...except...finally的错误处理机制；
- 注意
    - 如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获
'''
try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')
