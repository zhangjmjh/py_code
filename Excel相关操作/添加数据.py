



import os
import openpyxl

path = r'D:\api_code'
os.chdir(path)

workbook = openpyxl.load_workbook('test.xlsx')   # 返回一个workbook数据类型的值
# print(workbook.sheetnames)    # 打印Excel表中的所有表


sheet = workbook.active  # 获取活动表
data = [
    ['奥特曼',23],
    ['巴特',24],
]
for i in data:
    sheet.append(i)
workbook.save('test.xlsx')

#  往excel添加数据


