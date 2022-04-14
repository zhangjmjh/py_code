import requests
import ddddocr
from Health_app.config import config
from common.get_time import get_time

def get_image():
    url = config.admin() + "/user/headlineLogin/getCode"
    print(url)

    headers = {
        "content-type": "application/json",
        "versionName": config.versionName(),
        "systemType": "WEB",
        "Authorization": '',
        "timestamp": get_time()
    }

    response = requests.get(url=url,headers=headers)  # get 方法

    # 获取cookie
    cookies = response.cookies
    # print('1111111111')
    # print(response.cookies.items())
    cookie = requests.utils.dict_from_cookiejar(cookies)
    # print(cookie)
    # print(response.headers)

    # cookies = response.cookies.items()
    # cookie = ''
    # for name, value in cookies:
    #     cookie += '{0}={1};'.format(name, value)




    # print(response.content)  # 把验证码图片打印出来
    with open('./code.jpg', 'wb') as file:
        file.write(response.content)

    ocr = ddddocr.DdddOcr()
    with open('./code.jpg', 'rb') as f:
        images = f.read()
        res = ocr.classification(images)

    # 官网的cookie里面的参数 没什么实际意义
    # a = "33792E3D-3EB6-4161-8F48-20DEEF459E6C"
    # b = "1FE8E8C3-2061-4915-B9F1-8B18B0829650"

    CHECKCODE = cookie['CHECKCODE']
    JSESSIONID = cookie['JSESSIONID']

    # new_cookie = "p_h5_upload_u={};".format(a) + "p_h5_upload_clientId={};".format(b) + "JSESSIONID={};".format(JSESSIONID) + "CHECKCODE={}".format(CHECKCODE)
    new_cookie = "JSESSIONID={};".format(JSESSIONID) + "CHECKCODE={}".format(CHECKCODE)


    return res,new_cookie   # 返回验证码和cookie
    # print(res,new_cookie)

if __name__ == '__main__':
    get_image()

