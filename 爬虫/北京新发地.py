import requests
import json

url = "http://www.xinfadi.com.cn/getCat.html"

headers = {
        "user-agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46'
    }

data = {"prodCatid":1186}

# response = requests.post(url=url,headers=headers,json=data)
response = requests.post(url=url,headers=headers,data=data)
print(response.json())