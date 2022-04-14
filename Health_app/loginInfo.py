from common.web_sign_no import web_sign_no
from common.get_time import get_time
import requests
from Health_app.config import config
from get_imageCode import get_image
from login_admin import login


def loginInfo():
    res,new_cookie = get_image()

    url = config.admin() + "/user/headlineUser/loginInfo"
    # print(url)

    headers = {
        "content-type": "application/json",
        "sign": web_sign_no(),
        "systemType": "WEB",
        "timestamp": get_time(),
        "cookie": login()
    }

    response = requests.get(url,headers= headers)

    print(response.json())
    # pprint.pprint(response.json())

    # print(headers)

if __name__ == '__main__':
    loginInfo()