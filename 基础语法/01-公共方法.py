import os
import math,copy,random,time
from collections import Counter
import numbers as np  #  利用as关键字重命名函数包名 以后就可以直接用np


def hello_world():
    yourname = input('你好，请输入你的名字：')
    print('欢迎来到python时间',yourname)
    print('让我们开始学习吧')

# def study_number():
#     num1 = input('请输入一个数字：')
#     print('你输入的是数字%s'%num1,'可它的类型为：',type(num1))
#     num2 = int(input('再输入一个数字：'))
#     print('你输入的是数字%s'%num2,'它的类型为：',type(num2))
#     num3 = float(input('再输入一个数字：'))
#     print('你输入的是数字%s'%num3,'它的类型为:',type(num3))
#     print('num1 + num2={}'.format(int(num1) + num2))
#     print('num1 - num2={}'.format(int(num1) - num2))
#     print('num1 * num2={}'.format(int(num1) * num2))
#
#     print('num2/num3={:.4f}'.format(num2 / num3)) # 数字除法  保留小数点后4位
#     print('num2//num3={:.3f}'.format(num2 // num3))  # 数字整除，同时{:.3f}表示输出格式小数点后面保留三位
#     print('num2%num3)={:.4f}'.format(num2 % num3))


# study_number()

# class Users(): ##125、面向对象编程，python中创建类class，类包含有属性与方法，包括有私有变量，共有变量等等
#     def __init__(self,name,height,weight):
#         self.name = name
#         self.height = height
#         self.weight = weight
#         self.yanzi = 100
#
#     def display(self):
#         print('大家好，我是{}，身高{},体重{},颜值超高{}'.format(self.name,self.height,self.weight,self.yanzi))
#
# a = Users('zhangjm',120,120) # 133、实例化对象，创建Users类的实例
# a.display() # 134、对象调用方法


while(True):
    问话 = input('真人：')
    print('加机器人：'+问话.strip('吗？？')+"!")
