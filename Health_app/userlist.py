import json
import requests
from common.web_sign import get_sign
from login_admin import login
from Health_app.config import config
from common.get_time import get_time


def userlist():
    url = config.admin() + "/user/headlineUser/userList"

    data = {
        "userName": "",
        "phoneNumber": "",
        "userType": "",
        "channel": "",
        "contractUserType": 0,
        "enable": "",
        "createTimeS": "",
        "createTimeE": "",
        "loginChannel": "",
        "isBindPhone": "",
        "page": 1,
        "rows": 10
    }

    headers = {
        "content-type": "application/json",
        "versionName": config.versionName(),
        "sign": get_sign(data),
        "systemType": "WEB",
        "timestamp": get_time(),
        "cookie": login()
    }


    response = requests.post(url= url,data=json.dumps(data),headers= headers)

    print(response.json())
if __name__ == '__main__':
    userlist()