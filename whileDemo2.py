# 求0-100之间的偶数之和
# 方法1：
'''
i = 0
sum = 0
while i<=100:
    if(i % 2 == 0):
        sum += i
    i += 1
print(sum)
'''

# 方法2
i = 0
sum = 0
while i<=100:
    sum += i
    i += 2
print(sum)