

'''
a . 以参数名正序排序，排序前参数，例如Map参数：
{"statusReview":1,"endDate":"2021-10-14","terms":"","videoType":-1,"pageSize":20,"category":-1,"pageNum":1,"startDate":"2019-09-12","status":-1}

b. 排序后以&拼接，排序后参数末尾加上timestamp 和key：
category=-1&endDate=2021-10-14&pageNum=1&pageSize=20&startDate=2019-09-12&status=-1&statusReview=1&terms=&videoType=-1&timestamp=null&key=b0pDTrrfEn7zhnnLVRjmQG1pUzMrNt1M

c. 然后使用SHA1加密，加密后转换为16进制字符串，并转换为大写，
上面示例参数加密后的结果：ACF77787E4847AD9BDBE87D6962A14DFAB53D2B6

备注：
1.list参数逗号分隔,list内map排序转json,默认list内不嵌套list
2.参数传递方式通过通过content-type分为三种：
	1.url拼接，content-type为空或"application/x-www-form-urlencoded"；
	2.body传参，content-type为application/json；
	3.form表单传参，content-type为"application/x-www-form-urlencoded"
'''



# # 时间
# ts = time.time()
# timestamp = int(ts)
# print(timestamp)
#
# # 排序
# ret = {"statusReview":1,"endDate":"2021-10-14","terms":"","videoType":-1,"pageSize":20,"category":-1,"pageNum":1,"startDate":"2019-09-12","status":-1}
# new_res = "&".join(sorted([str(key)+"="+str(value) for key, value in ret.items()]))
# print(new_res)
#
# sign = new_res + "&" + "timestamp=" + str(timestamp) + "&" + "key=b0pDTrrfEn7zhnnLVRjmQG1pUzMrNt1M"
# print(sign)
#
# # sha1加密
# new_sing = hashlib.sha1(sign.encode("utf8")).hexdigest()
# print(new_sing)
#
#


import time
import hashlib

def get_sign(ret):
    t = time.time()
    timestamp = int(round(t * 1000))
    # print(timestamp)

    new_res = "&".join(sorted([str(key) + "=" + str(value) for key, value in ret.items()]))
    # print(new_res)

    sign = new_res + "&" + "timestamp=" + str(timestamp) + "&" + "key=JQz80G8xBQblioVgpD7kYbNWEmRgFpCi"
    # print(sign)

    app_sign = hashlib.sha1(sign.encode("utf-8")).hexdigest()
    # print(app_sign.upper())
    return app_sign.upper()


# if __name__ == '__main__':
#     data = {
#         "pageSize": 24,
#         "userPageSize": 20,
#         "deviceType": 1,
#         "firstChannelId": "2",
#         "firstChannelName": "推荐",
#         "imei": "jktt8C12D98DF14B449E9311A59CCC00BBF8",
#         "pageNum": 1
#     }
#     get_sign(data)















# a = {"statusReview":1,"endDate":"2021-10-14","terms":"1"}
# x = [str(key)+"="+str(value) for key, value in a.items()]
# print(x)
# x= "&".join(x)
# print(x)


# a = {"statusReview":1,"endDate":"2021-10-14","terms":"1"}
# for i, j in a.items():
#     print(i + "=" + str(j) + "&",end="")

# a = {"statusReview":1,"endDate":"2021-10-14","terms":"1"}
# res = dict(sorted(a.items(),key=lambda  x:x[0], reverse=False))
# res1 = dict(sorted(a.items()))
# print(res)
# print(res1)







