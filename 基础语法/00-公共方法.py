









# enumerate 在字典上是枚举、列举的意思 参数为可遍历/可迭代的对象(如列表、字符串)
# enumerate 多用于在for循环中得到计数，利用它可以同时获得索引和值，即需要index和value值的时候可以使用
# def get_number(ret, clc):
#     count = 0
#     for i, value in enumerate(ret):
#         if value == clc:
#             count += 1
#             print(clc, "出现的位置", i)
#     print(clc, "出现的次数", count)
# get_number("afasfasdf", "a")

# enumerate 方法举例
# a = "afasfasdf"
# for i in enumerate(a):
#     print(i)
# 结果
# (0, 'a')
# (1, 'f')
# (2, 'a')
# (3, 's')
# (4, 'f')
# (5, 'a')
# (6, 's')
# (7, 'd')
# (8, 'f')


# 写一个函数，默认求10的阶乘，也可以求其他数字的阶乘
# def get_factorial(n=10):
#     x = 1
#     for i in range(1, n + 1):
#         x *= i
#     return x
#
#
# print(get_factorial(5))  # 120


# 写一个函数 求多个数的平均值
# def num(*args):
#     x = 0
#     for i in args:
#         x += i
#     return x / len(args)
#
#
# print(num(1, 2, 3))  # 2.0


# 写一个capitalize函数 能够将指定字符串的首字母变成大写字母
# def capitalize(str):
#     c = str[0]
#     if 'z' >= c >= 'a':
#         new_str = str[1:]
#         return c.upper() + new_str
#     return str
#
#
# print(capitalize('rwerwrw'))  # Rwerwrw


# 写一个endwith函数 判断一个字符串是否以指定的字符串结束
# def endwith(ols_str,str1):
#     if ols_str[-len(str1):] == str1:
#     #     print('是')
#     # else:
#     #     print('否')
#
# endwith('hello','llo')  # 是

# 写一个isdigit函数 判断一个字符串是否是纯数字字符串
# def isdigit(str):
#     for i in str:
#         if not '0' <= i <= '9':
#             return False
#     return True
#
#
# print(isdigit('hee99'))  # False


# 写一个自己的max函数 获取序列中元素的最大值 如果序列是字典 获取字典的最大值
# def get_max(ret):
#     if type(ret) == dict:
#         ret = list(ret.values())
#     a = ret[0]
#     for i in ret:
#         if i > a:
#             a = i
#     return a
#
#
# print(get_max([2, 5, 8, 6, 3, 1]))  # 8

# revsersed 的用法  可对元组 字符串 以及 reange(n)的区间 返回一个逆序序列的迭代器
def ret(num):
    print([x for x in reversed(num)])
ret([1,2,3,4,5,5])  # [5, 5, 4, 3, 2, 1]

# 交换两个变量
a = 4
b = 5
a,b = b,a
print(a,b)  # 5 4

# 多个变量赋值
a,b,c = 4, 5.5, 'hello'
print(a, b, c)  # 4 5.5 hello

# 列表中偶数的和
a = [1,2,3,4,5,6]
s = sum([num for num in a if num%2==0])
print(s)  # 12

# 从列表中删除多个元素
a = [1,2,3,4,5,6,7]
del a[1::2]
print(a)  # [1, 3, 5, 7] 从下标为1的元素开始取，轮流取2位

# index() 查看索引
li = ['xxdd','sdd','形成',[1,3,4],'eeg','形成']
print(li.index('sdd'))   # 1

# count 出现的次数
print(li.count('形成')) # 2


# 使用 try、except、final 示例程序异常捕获
try:
    print(1 / 0)
except Exception as e:  # Exception 常规错误的基类
    print(e)
finally:  # 退出try时总会执行
    print("最后都会执行finally中的语句")




# Python 对象
class Person(object):
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def show(self):
        print('My name in {name}'.format(name=self.name))
        print('age:{age}'.format(age=self.age))
# 实例化对象
p1 = Person(age=18,name='zhangjm')
p1.show()


# Python的继承
class Man(Person):
    pass

# 子类实例化
man = Man(age=23, name='Case')
man.show()