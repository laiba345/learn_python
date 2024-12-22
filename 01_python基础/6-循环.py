# 遍历用户名字
names = ['kk', 'hk', 'hkk']; 
for name in names: 
    print(name); 

# 求和计算
sum = 0; 
for x in range(10): # 注意；range(5): 生成从0到5的所有整数（不包括5） 
    sum += x; 

print(sum); # 45

# break；可以提前结束循环
n = 1; 
while n <= 100:
    if n > 10: 
        break; 
    print(n); 
    n += 1; 
print('end'); 
print('---------------------------------------'); 
# continue; 提前结束本轮循环，并直接开始下一轮循环
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)