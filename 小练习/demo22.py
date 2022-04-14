

import random
def guess(num1,num2):

    if num2 == num1:
        return 0
    elif num2 > num1:
        return 1
    elif num2 < num1:
        return -1


num1 = random.randint(1,100)
for i in range(10):
    ret = int(input('请猜猜我心里的数吧：'))
    result = guess(num1,ret)
    if result == 0:
        print('猜对了')
        break
    elif result == 1:
        print('猜大了')
    elif result == -1:
        print('猜小了')
else:
    print('真笨，10次都猜不对')