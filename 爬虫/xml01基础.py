

from lxml import etree
parser = etree.HTMLParser(encoding='utf-8')
tree = etree.parse("b.html",parser=parser)

# result = tree.xpath("/html/body/ul/li/a/text()")  # ['百度', '搜狗', '谷歌']
# result = tree.xpath("/html/body/ul/li[1]/a/text()")  # ['百度']
# print(result)


# result = tree.xpath("/html/body/ol/li/a[@href='dapao']/text()")  # 只找到['大炮']的
# ol_li_list = tree.xpath("/html/body/ol/li")
# for i in ol_li_list:
#     result = i.xpath("./a/text()")   #  是从当前位置去查找，所以要用./
#     print(result)
#     result2 = i.xpath("./a/@href")   #  这里是拿到href的值
#     print(result2)


# print(tree.xpath("/html/body/ul/li/a/@href"))
#  ['http://www.baidu.com', 'http://www.sougou.com', 'http://www.google.com']

#  可以快速在页面上复制页面元素的xpath
print(tree.xpath('/html/body/div[1]/text()')) #  ['李嘉诚']

