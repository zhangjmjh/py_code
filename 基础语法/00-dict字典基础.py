# 字典

dict1 = {"color": "green", "points": 5}

# 查
print(dict1["color"])   # green

a = dict1.get("color")  # 查 get()
print(a)  # green
print(dict1.keys())  # dict_keys(['color', 'points'])
print(dict1.values())   # dict_values(['green', 5])
print(dict1.items())  # dict_items([('color', 'green'), ('points', 5)])


# 增加（没有就增加）
dict1["token"] = "123"
print(dict1)   # {'color': 'green', 'points': 5, 'token': '456'}

# 改 （有就修改）
dict1["token"] = "456"
print(dict1)   # {'color': 'green', 'points': 5, 'token': '456'}

# setdefault 设置默认  没有就增加
dic1 = {'age':18,'name':'xss','sex':'female'}
dic1.setdefault('weight',120)
print(dic1)  # {'age': 18, 'name': 'xss', 'sex': 'female', 'weight': 120}

# 有键值对，不做任何修改
dic1.setdefault('name','aa')
print(dic1)  # {'age': 18, 'name': 'xss', 'sex': 'female', 'weight': 120}

# pop 删除指定的键
dict2 = {"color": "green", "points": 5}
dict2.pop("color")
print(dict2)  # {'points': 5}

# 循环打印
dict2 = {"color": "green", "points": 5}
for i in dict2.keys():
    print(i)  # color   points  循环打印键
for i in dict2.values():
    print(i)  # green 5    # 循环打印值
for i in dict2.items():
    print(i)  # ('color', 'green')  ('points', 5)   注：打印键和值