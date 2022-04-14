

'''
推算日期
'''

import datetime
def inputdate():
    indate = input('请输入开始日期例如：(20200808)后按回车：')
    indate = indate.strip()  #  默认去除前后的空格
    datestr = indate[0:4] + "-" +indate[4:6] + "-" + indate[6:]
    return datetime.datetime.strptime(datestr,"%Y-%m-%d")   #  给一个字符串，给一个你需要转换的字符串格式

if __name__ == '__main__':
    sdate = inputdate()
    print(sdate)
    in_num = int(input('请输入间隔的天数：'))
    fdate = sdate + datetime.timedelta(days=in_num)
    print('您推算的日期是：'+ str(fdate).split(' ')[0]) #  首先根据空格来拆分,拆分完之后按照索引为0来展示,结果是不显示后面的00:00:00
    print(type(fdate))   #  <class 'datetime.datetime'>