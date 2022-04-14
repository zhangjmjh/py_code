list_1 = ['luoahong', 'chenqun', 'wenhai', 'daiqiao', 'xiedi', 'guiwei']

# 取值
a = list_1[0]
print(a)     #  结果：luoahong

# 切片
a = list_1[1:3]
print(a)    #  结果：['chenqun', 'wenhai']

# 增加元素
list_1.append("haha")
print(list_1)   #  结果：['luoahong', 'chenqun', 'wenhai', 'daiqiao', 'xiedi', 'guiwei', 'haha']

# 指定位置插入元素
list_1.insert(0, "xxx")
print(list_1)    #  结果：['xxx', 'luoahong', 'chenqun', 'wenhai', 'daiqiao', 'xiedi', 'guiwei']

# 修改
list_1[0] = "zjm"
print(list_1)    #  ['zjm', 'chenqun', 'wenhai', 'daiqiao', 'xiedi', 'guiwei']

# 删除
list_1.remove('guiwei')
print(list_1)   # ['luoahong', 'chenqun', 'wenhai', 'daiqiao', 'xiedi']

list_1.pop(0)  # 删除指定位置的元素
print(list_1)   # ['chenqun', 'wenhai', 'daiqiao', 'xiedi', 'guiwei']

# 排序
list_1.sort();
print(list_1)  #  ['chenqun', 'daiqiao', 'guiwei', 'luoahong', 'wenhai', 'xiedi']

list_1.sort(reverse=True)  # 降序
print(list_1)   #  ['xiedi', 'wenhai', 'luoahong', 'guiwei', 'daiqiao', 'chenqun']

# 获取下标
a = list_1.index('xiedi')
print(a)   # 0

# 列表去重
list1 = ['1', '1', '2', '2', '3', '3', '3']
list1 = list(set(list1))
print(list1)   # ['3', '2', '1']

# extend 追加到末尾
li = ['苹果','芒果','胡罗卜','香蕉']
li.extend('cc')
print(li)   # ['苹果', '芒果', '胡罗卜', '香蕉', 'c', 'c']

li.extend([1,2,3])
print(li)  # ['苹果', '芒果', '胡罗卜', '香蕉', 'c', 'c', 1, 2, 3]

# split字符串转换成列表str--list
li = 'xcsd_cdc_eht_哈哈'
print(li.split('_'))   # ['xcsd', 'cdc', 'eht', '哈哈']

# join 列表转换成字符串
li = ['苹果','芒果','胡罗卜','香蕉']
s = ''.join(li)
print(s)   # 苹果芒果胡罗卜香蕉  中间不留间隔合并成一个字符串
s = '_'.join(li)
print(s)   # 苹果_芒果_胡罗卜_香蕉


# sort 高级用法 给列表里面的字典来排序
student = [{'name': 'jerry', 'age': 80}, {'name': 'herry', 'age': 10}]
# student.sort(key=lambda ele: ele['name'])  # ele 可以随意定义
# print(student)
# 结果：[{'name': 'jerry', 'age': 80}, {'name': 'herry', 'age': 10}]