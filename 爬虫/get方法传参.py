import requests

#  第一种
response = requests.get('http://httpbin.org/get?name=zhangjm&age=20')  # get 传参
print(response.status_code)
print(response.text)


# 第二种
data = {
    'name':'zhangjm',
    'age':20
}

response = requests.get('http://httpbin.org/get',params=data)
print(response.status_code)
print(response.text)