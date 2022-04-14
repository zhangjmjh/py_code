import requests
import json


# 查询当前地点天气的url
url_city = "https://www.amap.com/service/cityList?version=2020101417"
# 各城市对应code的url
url_weather = "https://www.amap.com/service/weather?adcode={}"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
}

def get_city():
    # 查询所有城市名称和编号
    city = []
    response = requests.get(url=url_city,headers=headers)
    content = response.json()  # response.json()  是把返回响应的json字符串转换成字典
    # print(content)

    if "data" in content:
        cityByLetter = content['data']['cityByLetter']  # 这里是一级一级取出对象，data→cityByLetter  是我们要用到的对象
        for k, v in cityByLetter.items():  # 以列表返回可遍历的(键, 值) 元组数组
            city.extend(v)  # extend 接受一个参数，这个参数总是一个 list，并且把这个 list 中的每个元素添加到原 list 中
    return city

def get_weather(adcode,name):
    # 根据编号查询天气
    item = {}
    item["adcode"] = str(adcode)
    item["name"] = name

    response = requests.get(url=url_weather.format(adcode), headers=headers)  # url_weather.format(adcode) 这个链接需要传参，这是传参的一种方式
    content = response.json()
    # print(content)
    item["weather_name"] = content["data"]["data"][0]["forecast_data"][0]["weather_name"]
    item["min_temp"] = content["data"]["data"][0]["forecast_data"][0]["min_temp"]
    item["max_temp"] = content["data"]["data"][0]["forecast_data"][0]["max_temp"]


    print(item)

    return item

def save(item):
    # 保存
    print(item)
    with open("./weather.txt","a",encoding="utf-8")as file:
        file.write(','.join(item.values()))  # 用','来拼接字符  拼接的对象是item.values()  的值
        file.write("\n")

if __name__ == '__main__':
    get_weather('659004', '五家渠')
    # city_list = get_city()
    # for city in city_list:
    #     item = get_weather(city['adcode'],city['name'])
    #     save(item)










