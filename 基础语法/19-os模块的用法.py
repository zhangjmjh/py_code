import os # 调用操作系统里面的方法

# 获取操作系统的名字
print(os.name)  # nt-windows

# abspath 获取文件的绝对路径
print(os.path.abspath('00-公共方法.py'))  #E:\zhangjm_python\Python_code\00-公共方法.py

# isdir判断是否是文件夹
print(os.path.isdir('00-公共方法.py'))  # False

# isfile 判断是否是文件
print(os.path.isfile('00-公共方法.py')) # True

# exists 判断文件是否存在
print(os.path.exists('00-公共方法.py')) # True

# os其他方
os.getcwd()  # 查看当前文件路径