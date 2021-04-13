# 切片：从字符串中提取需要的部分；语法：序列名[开始的位置：结束的位置：步长]
# 不包括结束的位置，步长为正，表示从左向右，为负数则表示从右向左
numstr = "12345678"
# print(numstr[1:4])  # 234
# print(numstr[1:4:1])  # 234
# print(numstr[2:6:2])  # 35
# print(numstr[:])  # 只有冒号时打印出整个字符串
# print(numstr[2:])  # 345678
# print(numstr[:7])  # 1234567
#
# # 步长为负数
# print(numstr[::-1])  # 倒序打印字符串
# print(numstr[-1:-5:-1])  # 8765
# print(numstr[-7:-2])  # 23456
print(numstr[-7:-2:1])