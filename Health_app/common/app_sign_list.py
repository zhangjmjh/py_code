

import json
import time
import hashlib

def get_sign(ret):
#  这是APP签名，当参数为列表形式时的方法


	# 获取时间戳
	t = time.time()
	timestamp = int(round(t * 1000))

	# 对参数进行处理，转成字符串，拼接上逗号，然后去掉空格、加上双引号
	a = ''
	for i in ret:
		a = a + str(i) + ','
		res = a[0:-1]
		new_list_1 = res.replace(": ", ":")  # 把冒号后面的空格去掉
		new_list_2 = new_list_1.replace(", ", ",")  # 把逗号后面的空格去掉
		new_list = new_list_2.replace('\'', '\"')  # 把字符串的单引号变成双引号

	# 开始加密
	sign = new_list + "&" + "timestamp={}".format(str("timestamp")) + "&" + "key=JQz80G8xBQblioVgpD7kYbNWEmRgFpCi"
	app_sign = hashlib.sha1(sign.encode("utf-8")).hexdigest()


	# print(app_sign.upper())
	return app_sign.upper()



# if __name__ == '__main__':
# 	ret = [{
# 	"commodityCoder":"P20211230899401",
# 	"couponCoder":"GG90254570",
# 	"couponEndTime":"2025-06-30 00:00:00",
# 	"couponStartTime":"2021-05-20 00:00:00"
# }, {
# 	"commodityCoder":"P20211230899401",
# 	"couponCoder":"BB64516311",
# 	"couponEndTime":"2025-06-30 00:00:00",
# 	"couponStartTime":"2021-05-20 00:00:00"
# }]
# 	get_sign(ret)


# 处理字符串的第二种方法
# ls = []
# for i in old_list:
# 	x = json.dumps(i)
# 	print(x)
# 	ls.append(x)
# 	new_list = ','.join(ls)
# 	new_list = new_list.replace(" ","")
# print(new_list)



# print(timestamp)

# sign = new_list + "&" + "timestamp={}".format(str(timestamp)) + "&" + "key=b0pDTrrfEn7zhnnLVRjmQG1pUzMrNt1M"



# print(sign)








# ls = []
# for i in old_list:
# 	x = json.dumps(i)
# 	print(x)
# 	ls.append(x)
# print(','.join(ls))

















# list = [{
# 	"couponCoder": "SDFDS432432",
# 	"couponStartTime": "2022-02-10 00:00:00",
# 	"couponEndTime": "2022-02-25 00:00:00",
# 	"commodityCoder": "P20211230899401"
# }, {
# 	"couponCoder": "EREW23423",
# 	"couponStartTime": "2022-02-15 00:00:00",
# 	"couponEndTime": "2022-02-24 00:00:00",
# 	"commodityCoder": "P20211230899401"
# }, {
# 	"couponCoder": "BDDF3434",
# 	"couponStartTime": "2022-02-22 00:00:00",
# 	"couponEndTime": "2022-02-26 00:00:00",
# 	"commodityCoder": "P20211230899401"
# }]

# print("&".join(list))

# ret = {"statusReview":1,"endDate":"2021-10-14","terms":"","videoType":-1,"pageSize":20,"category":-1,"pageNum":1,"startDate":"2019-09-12","status":-1}
# new_res = "&".join(sorted([str(key)+"="+str(value) for key, value in ret.items()]))
# print(sorted(ret.items()))
# print(new_res)