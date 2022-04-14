
'''文件的读写的两种方式'''

fp = open('d:/案例1.txt','w')
print('奋斗成就更好的你',file=fp)
fp.close()


with open('d:/案例01.txt','w') as file:
    file.write('奋斗成就更好的你')

