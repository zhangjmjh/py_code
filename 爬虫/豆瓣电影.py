

import requests
import re
import csv

def get_douban():
    url = 'https://movie.douban.com/top250'
    headers = {
        "user-agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46'
    }
    respons = requests.get(url=url,headers=headers)
    page_content = respons.text


    # 开始解析数据
    find_title = re.compile(r'<span class="title">(.*?)</span>')  # 影片中文名
    find_href = re.compile(r'<a href="(.*?)">')  # 电影详情链接
    find_rating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')  # 评分
    find_judge = re.compile(r'<span>(.*?)人评价</span>')  # 评价人数
    find_inq = re.compile(r'<span class="inq">(.*?)</span>', re.S)  # 相关信息 re.S 将字符串看作一个整体



    # 开始匹配
    result = obj.finditer(page_content)
    for i in result:
        print(i.group('inq'))
        print(i.group('name'))
        # print(i.group('score'))
        # print(i.group('inq'))

if __name__ == '__main__':
    get_douban()