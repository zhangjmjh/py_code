#   千年虫案例


year = [82,89,88,86,00,99]

for index,value in enumerate(year):
    # print(index,value)  #   这里返回的是列表里面元素的序号和对应的值
    if str(value) != '0':
        year[index] = int('19' + str(value))
    else:
        year[index] = int('200' + str(value))
print(f'修改之后的值是：{year}')