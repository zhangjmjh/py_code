



# 元组  不能修改

tup = (1, 2, ['a', 'b', 'c'], 'd', 'e', ('gu', 'tang'), 1)

# 1、查询
# print(tup[0])    # 结果：1

# 2、列表转换成元组
li = ["python book", "Mac", "bile", "kindle"]
# tup = tuple(li)
print(tup)   # 结果：('python book', 'Mac', 'bile', 'kindle')

# 3、计算元组中元素的长度
print(len(tup))  # 结果： 6

# 4、统计元素出现的个数
print(tup.count(1))    # 结果：  2