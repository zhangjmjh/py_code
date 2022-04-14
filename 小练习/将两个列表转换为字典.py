








#   将两个列表转换为字典，常见的情况是一个列表作为键，另一个列表作为值来构造字典。




list1 = ['james','alice','hotl']
list2 = [88,86,96]

dict1 = dict(zip(list1,list2))
print(dict1)   #  {'james': 88, 'alice': 86, 'hotl': 96}