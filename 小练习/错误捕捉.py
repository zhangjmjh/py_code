


#

# try:
#     num1 = 10
#     num2 = 0
#     print(num1 / num2)
# except:
#     print('除数不能为0')



#   文件不存在
try:
    with open('./data.txt', 'r') as fr:
        print(fr.readline())
except IOError:
    print('该文件不存在')
finally:
    print('程序执行结束')
