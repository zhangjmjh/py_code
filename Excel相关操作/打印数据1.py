



import os
import openpyxl

path = r'D:\api_code'
os.chdir(path)

workbook = openpyxl.load_workbook('test.xlsx')
# print(workbook.sheetnames)    # 打印Excel表中的所有表


sheet = workbook.active  # 获取活动表
cell1 = sheet['A1':'A5']
for i in cell1:
    for j in i:
        print(j.value)


#  打印A1-A5的数据


