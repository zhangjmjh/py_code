import requests
from Health_app.common.app_sign import get_sign
from Health_app.config import config
from Health_app.common.get_time import get_time


def login():
    url = config.app() + "/user/headlineLogin/phoneLogin"

    data = {
        "verifyCode": "111111",
        "loginName": "17373110369",
        "inviteCode": ""
    }

    headers = {
        "content-type": "application/json",
        "versionName": config.versionName(),
        "sign": get_sign(data),
        "systemType": "iOS",
        "Authorization": '',
        "timestamp": get_time(),
        "devicetype": "iPhone Xs",
        "deviceid": "jktt8C12D98DF14B449E9311A59CCC00BBF8",
        "channel": "qd2021011202"
    }
    response = requests.post(url= url, json= data, headers= headers)

    # for i in response:
    #     print(i)
    #     status = response.json()['status']
    #     if status == 0:
    #         print("11111")
    #
    # token = response.json()['data']['token']
    # print(token)



    global token
    Authorization = str(response.json()['data']['token'])

    # print(Authorization)
    # print(response.json())
    return Authorization

    # print(response.headers)
    # print(headers)


if __name__ == '__main__':
    login()


