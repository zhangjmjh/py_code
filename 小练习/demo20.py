


def show(list):

    for item in list:
        for i in item:
            print(i, end='\t\t')
        print()
print('编号\t\t名称\t\t\t品牌\t\t单价')
list = [['01','电风扇','美的',500],
        ['01','洗衣机','美的',900],
        ['01','微波炉','美的',200]]

# print('编号\t\t名称\t\t\t品牌\t\t单价')
show(list)


print('编号\t\t\t名称\t\t\t品牌\t\t\t单价')
for item in list:
    item[0] = '0000' + item[0]
    item[3] = '￥{:.2f}'.format(item[3])
show(list)
