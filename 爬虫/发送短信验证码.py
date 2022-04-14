import requests
import json
import time

url = "https://tbk.dgdell.com/?act=ucenter&ctrl=getCode"

data = {"code":"17373110369"}


headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"}



for i in range(1,50):
    res = requests.post(url = url,data = data,headers = headers)
    time.sleep(1)

    print(res.json())


# for i in range(1,10):
#     print('111')