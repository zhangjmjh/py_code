import requests
from SHEIN.config import config


def comment_login():
    url = config.app() + "/user/common_login"

    data = {
        "challenge": "1d6c7acce211d77af6616ff82cf83b2c",
        "clause_agree":"",
        "clause_country_id": 0,
        "clause_flag": 0,
        "email": "zhangjm.jh@qq.com",
        "password": "shein123",
        "risk_id": ""
    }

    headers = {
        'AppVersion': config.AppVersion(),
        'DeviceId': '5df652aec2cd07df6db49c9928225e6f',
        'skipGeetest': '1',
        'SiteUID': 'app',
        "Content-Type": "application/x-www-form-urlencoded"
    }
    response = requests.post(url= url, data= data, headers= headers)

    # for i in response:
    #     print(i)
    #     status = response.json()['status']
    #     if status == 0:
    #         print("11111")
    #
    # token = response.json()['data']['token']
    # print(token)



    # global token
    Authorization = str(response.json()['info']['member']['token'])

    print(Authorization)
    print(response.json())
    # return Authorization

    # print(response.headers)
    print(headers)

if __name__ == '__main__':
    comment_login()


