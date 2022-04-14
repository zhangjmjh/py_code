




# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f'{i}*{j}={i*j}',end= ' ')
#     print()


for i in range(1,10):
    for j in range(1,i+1):
        print(f'{i}*{j}={i*j}',end=' ')
    print()





# def get_num(list,target):
#     count = 0
#     for i,j in enumerate(list):
#         if j == target:
#             print(target,'出现的位置：',i)
#             count += 1
#     print(target,'出现的次数:',count)
#
# get_num('werwerwerdfasd','w')

def get_num(str,target):
    count = 0
    for i ,j in enumerate(str):
        if j == target:
            print(target,'出现的位置：',j)
            count += 1
    print(target,'出现的次数：',count)

get_num('qwerqrqwe','w')



list = [5, 23, 3, 2, 54, 4, 6, 8, 856]
# list_len = len(list)
# for i in range(list_len-1):
#     for j in range(i,list_len):
#         if list[i] > list[j]:
#             list[i],list[j] = list[j],list[i]
# print(list)
lis_len = len(list)
for i in range(lis_len-1):
    for j in range(i,lis_len):
        if liss[i] > list[j]:
            list[i],list[j] = list[j],list[i]
print(list)

#
# from functools import reduce
#
# n = 5
# print(reduce(lambda x,y:x*y,range(1,n+1)))
#



# 根据指定的value找到对应的key
dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}

'''
先打印出所有的key和value,转换为列表
因为字典里面key和value是一一对应的
所以找到value里面的索引，再根据索引找到key列表的值

'''

print(dict['Alice'])







