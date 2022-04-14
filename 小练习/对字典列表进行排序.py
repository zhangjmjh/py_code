

dict1 = [
    {'name':'oppo','num':25},
    {'name':'vivo','num':26},
    {'name':'apple','num':45}
]

#  利用sort排序
dict1.sort(key=lambda item: item['num'])
print(dict1)    #  [{'name': 'oppo', 'num': 25}, {'name': 'vivo', 'num': 26}, {'name': 'apple', 'num': 45}]

# 利用sorted排序
dict1 = sorted(dict1, key=lambda item: item["num"])
print(dict1) #  [{'name': 'oppo', 'num': 25}, {'name': 'vivo', 'num': 26}, {'name': 'apple', 'num': 45}]