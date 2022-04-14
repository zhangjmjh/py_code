




#    创建表和数据


import xlsxwriter
import os


path = r'D:\api_code'
os.chdir(path)

# 创建一个名为 demo.xlsx 的工作簿
workbook = xlsxwriter.Workbook('接口测试脚本.xlsx')

# 创建一个名为 2018年销售量 工作表
worksheet = workbook.add_worksheet('2018年销售量')

# 使用write_row方法，为该表添加一个表头
headings= ['产品','销量','单价']
worksheet.write_row('A1',headings)

# 使用write方法，在表中插入一条数据
# write语法格式：worksheet.write(行，列，数据)

data = ['苹果',500,8.9]
for i in range(len(data)):
    worksheet.write(1, i, data[i])   # i 分别取值 0 1 2 表示第一列 第二列 第三列     data[i] 分别取值 '苹果' 500 8.9
workbook.close()








