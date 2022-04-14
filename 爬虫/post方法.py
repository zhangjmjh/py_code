import requests


response = requests.post('http://httpbin.org/post') #  post方法
print(response.status_code)
print(response.text)