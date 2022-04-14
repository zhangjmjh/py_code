import json
import requests
import pprint
from Health_app.common.get_time import get_time
from Health_app.common.app_sign import get_sign
from Health_app.config import config
from login import login



def getHealthCircleList():
    url = config.app() + "/search/search/getHealthCircleList"

    data = {
        "pageNum": 1,
        "pageSize": 16
    }

    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "versionName": config.versionName(),
        "sign": get_sign(data),
        "systemType": "iOS",
        "Authorization": login(),
        "timestamp": get_time(),
        "devicetype": "iPhone Xs",
        "deviceid": "jktt8C12D98DF14B449E9311A59CCC00BBF8",
        "channel": "qd2021011202"
    }

    response = requests.post(url=url, data=data, headers=headers)
    print(response.json())
    print(headers)

    for i in response.json()['data']:
        isTop = i['isTop']
        if isTop == 0:
            print(i['id'])
            break



if __name__ == '__main__':
    getHealthCircleList()