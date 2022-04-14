dict_ticket = {
    'G1509' : ['北京南-天津南','18:05','18:36','18:45'],
    'G1567' : ['北京南-天津南','18:05','18:36','18:45'],
    'G8917' : ['北京南-天津南','18:05','18:36','18:45'],
    'G203' : ['北京南-天津南','18:05','18:36','18:45']
               }

print('车次\t\t出发站-到达站\t\t出发时间\t\t到达时间\t\t历时时长')
for item in dict_ticket:
    print(item,end='   ')  # 末尾不换行 添加空格
    for i in dict_ticket[item]:  #  根据键获取值
        print(i , end='    ') # 末尾不换行 添加空格
    print()  # 换行

train_no = input('请输入要购买的车次:')
persons = input('请输入乘车人，如果是多人请使用逗号分割:')

s = dict_ticket[train_no][0] + ' ' + dict_ticket[train_no][1] + '开'
print(f'您已购买了{train_no}，{s}请{persons}尽快取走纸质车票。谢谢')
