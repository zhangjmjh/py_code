




#  对于检查列表中是否有重复的元素，可以通过将列表转换为set来快速检查


list1 = [1,2,3,2,5,6,7]
list2 = [1,2,3,4,5,6,7]

print("list1有重复元素：", len(list1) != len(set(list1)))   #  结果返回true   或者  false  