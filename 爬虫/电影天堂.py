import requests



url = "https://m.dytt8.net/index2.htm"
response = requests.get(url=url)
response.encoding = 'gbk'
print(response.text)
