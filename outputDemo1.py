name = 'tom'
age = 18
stuId = 190021
stuId2 = 1
weight = 55.22
sex='男'
print('my name is %s' % name)
print('年龄是：%d' % age)
print('学号是：%s' % stuId)
print('体重是：%.2f' % weight)

print('我的名字是%s,今年%d岁,体重是%.2f公斤,学号是%04d' % (name,age,weight,stuId2))

print('%s明年%d岁了' % (name,age+1))
print('我的名字是%s,今年%s岁,体重是%s公斤,学号是%s' % (name,age,weight,stuId2))

# f格式化字符
print(f'我的名字是{name},今年{age}岁')
print(f'我的名字是{name},今年{age+1}岁')

# 转义字符
print('hello\nworld')  # \n:换行
print('名字\t年龄\t性别\t学号')
print(f'{name}  \t{age}  \t{sex}  \t{stuId}')

print('%s  \t%d  \t%s  \t%s' % (name,age,sex,stuId))


# print结束符：print（内容，end=''）
print('hello',end='...')
print('world')