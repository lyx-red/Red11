# 先判断有没有钱，有钱则可以上车，否则不可以上车
# 上车之后要判断是否有座位，有则坐下，否则站着
money = int(input('请输入是否有钱（1表示有，0表示无）：'))

if money == 1:
    print('可以上车')
    seat = int(input('请输入是否有座位（1表示有，0表示无）：'))
    if(seat == 1):
        print('有座位，可以坐下')
    else:
        print('没有座位，站着')
else:
    print('上不了车')