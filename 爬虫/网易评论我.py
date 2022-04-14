import requests
import json
import time
from wordcloud import WordCloud
import jieba
import numpy
import PIL.Image as Image  # 图像处理的库
import io   # 读写文件的库




def get_all_comments(id,page):
    comment_path = "./wangyicoments.txt"
    base_url = "http://music.163.com/api/v1/resource/comments/R_SO_4_" + id + "?limit=20&offset="
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
    }

    for i in range(page):
        sffset = i * 20
        url = base_url + str(sffset)
        res = requests.post(url=url, headers=headers)
        comments = json.load(res.text)
        if ("hotComments" in comments):
            comments = comments['hotComments']
        else:
            comments = comments['comments']




    pass

if __name__ == '__main__':
    id = int(input('请输入需要爬取的歌曲ID：'))
    page = int(input('请输入需要爬取歌曲评论的页数：'))
    get_all_comments(id=id, page=page)