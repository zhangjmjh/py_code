# 快递查询工具

import json,requests

# def searchPackage():
#     # 输入运单号码，注意，只有正在途中的快递才可以查询
#     packageNum = input("请输入运单号码：")
#     headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
#     url1 = "https://www.kuaidi100.com/autonumber/autoComNum?text=" + packageNum
#
#     # 根据url1查询运单号对应的快递公司
#     # json.dumps()函数是将字典转化为字符串
#     # json.loads()函数是将字符串转化为字典
#     compantName = json.loads(requests.post(url1,headers=headers).text
#
#     # 使用url2来查询快递详情
#     # url2 = 'https://www.kuaidi100.com/query?type=' + compantName + '&postid=' + packageNum
#     #
#     # print('时间↓                                                  地点和跟踪进度↓\n')
#     # for i in json.loads(requests.get(url2).text)['data']:
#     #     print(['time'],['context'])
#
#
# searchPackage()

# headers = {'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
url = "https://www.kuaidi100.com/autonumber/autoComNum?text=4312200416625"
a = requests.post(url,headers=headers)
print(a.text)
