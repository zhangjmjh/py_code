








#    当大家需要对一个字符串列表进行排序时，可以利用下图中的程序进行排序。





list1 = ['james','alice','hotom','cris']


# print(sorted(list1, key=lambda x:x. lower()[0]))  # 按照字符串的第一个字母排序

print(sorted(list1, key=lambda x:x [0]))         # 按照字符串的第一个字母排序
print(sorted(list1, key=lambda x:x [-1]))         # 按照字符串的最后一个字母排序

  #   ['alice', 'cris', 'hotom', 'james']
# lower()  将所有大写字母转换成小写字母


