age = int(input('请输入您的年龄：'))
if age<18:
    print(f'你的年龄是{age}岁，您还未成年，不能参加工作')
elif 18<=age<=60:
    print(f'你的年龄是{age}岁，您已成年，可以参加工作')
else:
    print(f'你的年龄是{age}岁，您已可以退休')