import requests
from Health_app.common.get_time import get_time
from Health_app.common.app_sign import get_sign
from Health_app.config import config


def tuijian():
	# url = "https://zixun.001pt.com/search/search/getRecommendData2"
	url = config.app() + "/search/search/getRecommendData2"

	data = {
  "imei": "jktt8C12D98DF14B449E9311A59CCC00BBF8",
  "deviceType": 1,
  "pageNum": 1,
  "pageSize": 24,
  "firstChannelId": "2",
  "userPageSize": 20,
  "firstChannelName": "推荐"
}

	headers = {
		"content-type" : "application/json",
		"versionName" : config.versionName(),
		"sign" : get_sign(data),
		"systemType" : "iOS",
		"Authorization" : "token",
		"timestamp" : get_time(),
		"deviceType": "iPhone Xs",
		"deviceId": "jktt8C12D98DF14B449E9311A59CCC00BBF8"
	}

	response = requests.post(url=url, json=data, headers=headers)


	###########  以下是断言部分 ###############

	# assert response.json()['msg']=='查询列表成功'   #  这是json的断言

	# print(jsonpath(response.json(), '$..msg'))  #  ['查询列表成功']   这里必可以打印出来
	# assert jsonpath(response.json(), '$..msg')[0] == '查询列表成功'    #  必须要加[0]   不然的话断言会失败，就是上次有中括号的那个

	# assert_that(response.json()['msg'], equal_to('查询列表成功'))  #  这个断言果然好用

	print(response.json())
	# pprint.pprint(response.json())
	# print(response.headers)
	# print(headers)

if __name__ == '__main__':
	tuijian()
