import requests

url = 'http://www.baidu.com'
response = requests.get(url)
response.encoding = "utf=8"
print("\nr的类型"+str(type(response)))
print("\n状态码是："+str(response.status_code))
print("\n头部信息："+str(response.headers))
print("\n响应内容：")
print(response.text)

file = open("/Python_code\\爬虫\\baidu.html", "w", encoding="utf-8")
file.write(response.text)
file.close()