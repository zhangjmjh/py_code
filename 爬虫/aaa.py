

# list=['1','2','3','a','b','c']
# print("*".join(list))


# list = [2,34,5,66345,547,4,2,6,]
# for i in list:
#     if i == 2:
#         print(i)

# dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
# key = list(dict.keys())
# value = list(dict.values())
# print(key)
# print(value)
#
# index = value.index('2341')
# print(index)
# print(key[index])



list_1 = [1, 2, 3, 4]

list_2 = ['a', 'b', 'c']

# for i, j in enumerate(list_2):
#     print('遍历出来的下标是{0},值是{1}'.format(i,j))

# for i, j in zip(list_2):
#     print('遍历出来的下标是{0},值是{1}'.format(i,j))

dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
for i, j in dict.items():
    print(i,j)