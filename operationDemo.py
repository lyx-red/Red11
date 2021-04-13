# 算术运算符
a = 10
b = 3
print(f'{a}+{b}={a+b}')
print(f'{a}-{b}={a-b}')
print(f'{a}*{b}={a*b}')
print(f'{a}/{b}={a/b}')
print(f'{a}//{b}={a//b}')  # //整除
print(f'{a}%{b}={a%b}')
print(f'{a}**{b}={a**b}')  # **求幂

# 赋值运算符
num=11
print(num)

# 多个变量赋值
a,b,c = 11,2.3,'2332'
print(a,b,c)

# 多个变量赋相同的值
d = e = 11
print(d,e)


# 逻辑运算符
num1=2
num2=4
print((num1>num2) and (num1<num2))
if(num1<num2):
    print(True)
else:
    print(False)

print((num1>num2) or (num1<num2))
print(not(num1>num2))

print(2 and 3) # 都不为零时返回最后一个非零数字
print(0 or 9)  # 若有一个不为零，则返回第一个非零数字