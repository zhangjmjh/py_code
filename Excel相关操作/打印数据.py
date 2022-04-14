



import os
import openpyxl

path = r'D:\api_code'
os.chdir(path)

workbook = openpyxl.load_workbook('test.xlsx')
# print(workbook.sheetnames)    # 打印Excel表中的所有表


sheet = workbook.active  # 获取活动表
cell1 = sheet['A1']
print(cell1.value)


#  打印单列的数据
