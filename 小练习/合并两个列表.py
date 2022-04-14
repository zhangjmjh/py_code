

list1 = ['1','2','3','4']
list2 = ['one', 'two', 'three', 'four']


new_list = [x + y for x,y in zip(list1,list2)]
print('两个列表的合并：', new_list)   #  两个列表的合并： ['1one', '2two', '3three', '4four']