

import re

# findall:  匹配字符串所有的符合正则的内容
list = re.findall('\d+','我的电话号是：10086,其他人的电话是：10010')
print(list)  # ['10086', '10010']


# finditer:  匹配字符串中所有的内容，返回的是迭代器,迭代器就可以遍历
it = re.finditer('\d+','我的电话号是：10086,其他人的电话是：10010')
for i in it:
    print(i.group())   # 10086  10010

# re.search  找到一个结果就返回
se = re.search('\d+','我的电话号是：10086,其他人的电话是：10010')
print(se.group())  # 10086


# 预加载正则表达式
obj = re.compile('\d+')

# 下面正常开始写匹配的代码

# ?P<>  就是我要的变量名
s = """
<div class='jay'><span id='1'>郭靖</span></div>
"""

                                                               # re.S 让.能匹配换行符
obj = re.compile("div class='.*?'><span id='(?P<id>\d+)'>(?P<wahaha>.*?)</span></div>", re.S)
result = obj.finditer(s)
for it in result:
    print(it.group('wahaha'))