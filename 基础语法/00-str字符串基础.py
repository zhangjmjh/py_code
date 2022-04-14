# 字符串
a = 'afasdfasdf'

# 访问字符串中的值
var1 = 'Hello World!'
print(var1[0]) # 结果：H

# 字符串连接
var1 = 'Hello World!'
print(var1+'haha') # 结果：Hello World!haha

# 格式化字符串  %s 格式化字符串  %d 格式化整数
print("My name is %s and weight is %d kg!" % ('Zara', 21))
# 结果：My name is Zara and weight is 21 kg!

# 字符串切片
txt = "Google#Runoob#Taobao#Facebook"
x = txt.split("#", 1)  # 以#号作为分割 第二个参数为 1，返回两个参数列表
# print(x)  # ['Google', 'Runoob#Taobao#Facebook']

# 将数字转换成字符串
tt = 322
tem = '%d' % tt
print(tem)  # 322
print(type(tem))  # <class 'str'>