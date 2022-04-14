



#   打印水仙花数
# 假设 i y z 分别是这个3位数的百位数、十位数、个位数
# 既有：(i*100)+(y*10)+z = i**3 + y**3 + z**3

for i in range(1,10):
    for y in range(0,10):
        for z in range(0,10):
            num1 = i*100 + y*10 + z
            num2 = i**3 + y**3 + z**3
            if num1 == num2:
                print(f'水仙花数有{num1}')