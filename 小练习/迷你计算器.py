


''''
迷你计算器
'''



def get_num(a,b,cu):
    if cu == '+':
        return add(a,b)
    elif cu == '-':
        return sub(a,b)
    elif cu == '*':
        return op(a,b)
    elif cu == '/':
        if b != 0:
            return div(a, b)
        else:
            return '除数不能等于0'
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def op(a,b):
    return a*b
def div(a,b):
    return a/b

if __name__ == '__main__':
    a = int(input('请输入第一个整数：'))
    b = int(input('请输入第二个整数：'))
    cu = input('请输入运算符：')
    print(get_num(a, b, cu))
