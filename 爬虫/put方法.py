import requests

response = requests.put('http://httpbin.org/put') # put方法
print(response.status_code)
print(response.text)