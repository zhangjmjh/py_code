# 将指定的十进制数转换成二进制、八进制、十六进制
def fun():
    while True:

        try:
            num = int(input('请输入一个十进制的整数：'))
            print(num,'的二进制数为：',bin(num))  # 使用了个数可变的位置参数
            print(str(num)+'的二进制数为：' + bin(num))   #  使用 + 号做拼接符 + 号左右均为str类型
            print('%s的二进制数为：%s' % (num,bin(num)))     #  格式化字符串
            print('{0}的二进制数为{1}'.format(num,bin(num)))   # 格式化字符串 0：表示取第一个数  1：取第二个数
            print(f'{num}的二进制数为：{bin(num)}')  # 格式化字符串

            print(f"{num}的二进制数为：{oct(num)}")  #  转换成八进制
            print(f"{num}的二进制数为：{hex(num)}")  #  转换成十六进制

            break

        except:
            print('只能输入整数，程序出错，请重新输入')
            
if __name__ == '__main__':
    fun()