import requests
import json
import urllib
import time


def getSouImage(category,length):
    cate = category
    n = length
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    }
    url = "https://pic.sogou.com/pics/channel/getAllRecomPicByTag.jsp?category="+cate+"&tag=%E5%85%A8%E9%83%A8&start=45&len="+str(n)+"&width=1920&height=1080"

    path = r'D:\image'
    ret_time = time.strftime('%H:%M:%S', time.localtime())

    imgs = requests.get(url=url, headers=headers)

    jd = json.loads(imgs.text)
    jd = jd['all_item']
    image_url = []
    for i in jd:
        image_url.append(i['bthumbUrl'])
    m = 0
    for j in image_url:
        # print('正在爬取第{}张图片'.format(m))
        urllib.request.urlretrieve(j, path + str(m)+ '.jpg')
        m += 1
    print('下载完成')
if __name__ == '__main__':
    getSouImage('壁纸', 10)

