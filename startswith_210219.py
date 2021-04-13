# 语法：字符串名.startswith[字串，开始的位置，结束的位置]
# 判断是否以该字串开头
str1 = "My name is Tylor"
# print(str1.startswith("name"))

print(str1.startswith("My", 0, 1))
print(str1.startswith("My", 0, 4))