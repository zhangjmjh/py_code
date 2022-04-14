

# 面向对象编程
import math
class Circle(object):  #  类的名字第一个字母大写，默认继承object对象，不写也可以
    def __init__(self,r):  # 定义一个默认的init初始化函数
        self.r = r  #  继承

    def get_area(self):  #  求圆的面积
        return math.pi*math.pow(self.r,2)    #  求平方
    def get_perimeter(self):
        return 2*math.pi*self.r

if __name__ == '__main__':
    r = int(input('请输入圆的半径：'))
    c = Circle(r)  #  创建这个圆的对象
    print(f'圆的面积为：{c.get_area()}')
    print(f'圆的周长为：{c.get_perimeter()}')
    print('圆的周长为：{:.2f}'.format(c.get_area()))
    print('圆的周长为：{:.2f}'.format(c.get_perimeter()))
