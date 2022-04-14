from lxml import etree


# parser = etree.HTMLParser(encoding='utf-8')
# tree = etree.parse("b.html",parser=parser)
#
# failures_num = tree.xpath('//*[@id="failureNum"]/text()')[0]
#
# result = tree.xpath('/html/body/div[3]/div[1]')
# for i in result:
#     new_result = i.xpath("./table/tbody/tr[3]/td[3]/text()")
#     print(new_result)


fp = open('D:/test_app/report/html/TestReport.html','rb')
html = fp.read().decode('utf-8')
# print(html)
tree = etree.HTML(html)
failures_num = tree.xpath('//*[@id="failureNum"]/text()')[0]
print(failures_num)
# result = tree.xpath('/html/body/div[3]/div[1]')
# for i in result:
#     new_result = i.xpath("./table/tbody/tr[3]/td[3]/text()")
#     print(new_result)

result = tree.xpath('//*[@id="responseTime]')
print(result)