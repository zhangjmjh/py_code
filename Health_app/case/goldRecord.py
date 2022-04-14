import requests
from Health_app.common.app_sign import get_sign
from Health_app.config import config
from Health_app.common.get_time import get_time
from Health_app.case.login import login
import json
import jsonpath


def goldRecord():
    url = config.app() + "/gold/goldRecord/queryByUserId?isToDay=0&pageNum=1&pageSize=20"

    headers = {
        "content-type": "application/json",
        "versionName": config.versionName(),
        # "sign": get_sign(data),
        "systemType": "iOS",
        "Authorization": login(),
        "timestamp": get_time(),
        "devicetype": "iPhone Xs",
        "deviceid": "jktt8C12D98DF14B449E9311A59CCC00BBF8",
        "channel": "qd2021011202"
    }
    response = requests.get(url= url, headers= headers)


    # data = response.json()['data']['list']
    data = response.json()
    print(type(data))
    a =json.dumps(data)
    print(type(a))

    # for i in data:
    #     print(i['changeType'])

    # a = jsonpath.jsonpath(data,'$..id')
    # print(a)




    # print(data)

    # ls = []
    # for i in data:
    #     x = json.dumps(i)
    # print(type(x))
    # 	ls.append(x)
    # 	new_list = ','.join(ls)
    # 	new_list = new_list.replace(" ","")
    # print(data)

if __name__ == '__main__':
    goldRecord()


