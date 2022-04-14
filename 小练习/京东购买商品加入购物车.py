


# 京东购买商品加入购物车


list = []
for i in range(1,5):  #
    ret = input('请输入要加入的商品编号和商品名称，一次只能输入一件商品：')
    list.append(ret)
print(list)

cats = []
while True:
    res = input('请输入要购买的商品编号：')
    for item in list:
        if item.find(res) == 0:  # 如果在item里面找到了res，也就是条件为真等于1的情况下，把商品加到购物车中
            cats.append(item)
            print(item)
            break  # 添加完商品后就退出循环
    if res == 'q':
        break #  退出while循环
print('您的购物车商品为：')
for i in range(len(cats)-1,-1,-1):   #  逆序输出  最后一个-1是步长
    print(cats[i])  # i 是索引



'''
list = ['1001 手机', '1002 华为', '1003 小米', '1004 三星']
for i in list:
    # print(type(i[0]))
    if i.find('1001') == 0:
        print('我找到了')
1、i 遍历到的数据都是字符串类型，这里之所以要加循环去遍历，是因为find()方法不支持列表 只支持字符串 
2、if 的条件判断是如果从i里面找到了字符串"1001" 条件为真 ==0  才会打印  一定要加个条件 ==0 或者 != -1 才会走下一步
'''
