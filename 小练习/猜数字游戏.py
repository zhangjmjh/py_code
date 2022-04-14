


#    猜数字游戏

import random
rand = random.randint(1,100)

for i in range(1,11):
    num = int(input('我心中有个数字1-100，请你猜一猜:'))
    if num < rand:
        print('小了')
    elif num > rand:
        print('大了')
    else:
        print('恭喜你猜对了')
        break
print(f'您一共猜了{i}次')
if i < 3:
    print('真聪明')
elif i <7:
    print('还凑合吧')
else:
    print('你真的是笨蛋啊')