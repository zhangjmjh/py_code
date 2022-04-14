

import requests


# def test_demo():
#     url = "https://zixun-mp.001pt.com/user/headlineLogin/phoneLogin"
#     data = {"platform":"healthnum","verifyCode":"111111","loginName":"17373110369","source":2}
#
#     t = time.time()
#     timestamp = str(round(t * 1000))
#
#     headers = {
#         "content-type": "application/json",
#         "versionName": '1.5.0',
#         "sign": new_sign(data),
#         "systemType": "WEB",
#         "Authorization": '',
#         "timestamp": timestamp,
#         "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
#     }
#     response = requests.get(url = url, headers=headers)
#     print(response.headers)


def test_demo():
    url = "https://httpbin.testing-studio.com/cookies"
    headers = {"Cookie":"test"}
    respons = requests.get(url= url, headers= headers)
    print(respons.request.headers)

if __name__ == '__main__':
    test_demo()