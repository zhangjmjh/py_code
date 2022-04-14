


coffee = ('蓝山','卡布奇洛','拿铁','女王咖啡')
print('您好：欢迎光临小猫咖啡')
print('本店经营的咖啡有：')
for index,item in enumerate(coffee):
    print(index+1,'.',item,end='  ')   #  end=''  末尾不换行

ret = int(input('请输入您要选择的咖啡编号：'))
if 0 <= ret <= len(coffee):
    print(f'您的咖啡[{coffee[ret-1]}]好了，请您慢用')
