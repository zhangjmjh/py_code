import requests
import json
from common.get_time import get_time
from common.web_sign_list import web_sign_list
from get_imageCode import get_image
from Health_app.config import config



def login():
    res,new_cookie = get_image()

    url = config.admin() + "/user/headlineLogin/login"

    data = {
        "checkCode": res,
        "loginName": "zhangjianming",
        "password": "naBrcnmC+Jvib2TBOgeWRvussC933g1dNsSyleoqbSmF5nmGaJNw1lzFrtDxZ2D3Dp5DiSBiieOisZsaYKOPOghbdpHS1O7SuCO3mmCIcM+TTe/62a8kwk0BVBH0fPqeIO0yXjIzsgNMt03UxiWYv1luhMB6xeE0XRaM3NuPKTI="
    }

    headers = {
        "content-type": "application/json",
        "sign": web_sign_list(data),
        "systemType": "WEB",
        "timestamp": get_time(),
        "cookie": new_cookie
    }

    response = requests.post(url= url, data= json.dumps(data), headers= headers)

    # print(response.json())
    # print(data)
    # print(headers)
    # print(response.status_code)

    cookies = response.cookies
    cookie = requests.utils.dict_from_cookiejar(cookies)
    AUTH_TICKET = cookies['AUTH_TICKET']
    # print(new_cookie + ";" + "AUTH_TICKET={}".format(AUTH_TICKET))

    new_cookie = new_cookie + ";" + "AUTH_TICKET={}".format(AUTH_TICKET)
    return new_cookie + ";" + "AUTH_TICKET={}".format(AUTH_TICKET)

#
if __name__ == '__main__':
    login()


