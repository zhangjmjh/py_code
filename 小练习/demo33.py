'''
记录用户操作日志haha
'''

import time

def show_info():
    print('输入提示的数字，执行相应的操作：0:退出   1:查看登陆日志')


#  记录日志
def write_logininfo(username):
    with open('log.txt','a') as file:  #  上下文管理器,可以不用退出
        s = f'用户名{username},登陆时间:{time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))}'
        file.write(s)

# 读取日志
def read_logininfo():
    with open('log.txt','r') as file:
        while True:
            line = file.readlines()
            if line == '':
                break
            else:
                print(line)

if __name__ == '__main__':


    '''print(time.time())  #  1621778271.1951826
    print(time.localtime(time.time()))  # time.struct_time(tm_year=2021, tm_mon=5, tm_mday=23, tm_hour=21, tm_min=57, tm_sec=51, tm_wday=6, tm_yday=143, tm_isdst=0)
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))  # 2021-05-23 21:58:14'''

    username = input('请输入用户名：')
    pwd = input('请输入密码：')
    if 'admin' == username and 'admin' == pwd:
        print('登陆成功')
        write_logininfo(username)   # 记录日志
        show_info()  # 提示用户要执行什么操作
        num = int(input('输入操作数字：'))
        while True:
            if num == 0:
                print('退出成功')
                break
            elif num == 1:
                print('查看登陆日志')
                read_logininfo()   #  读取日志
                num = int(input('输入操作数字：'))
            else:
                print('您输入的数字有误')
                show_info()
                num = int(input('输入操作数字：'))

    else:
        print('对不起，用户名或密码不正确')
