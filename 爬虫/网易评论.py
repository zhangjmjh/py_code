

import requests
import json
import time
from wordcloud import WordCloud
import jieba
import numpy
import PIL.Image as Image  # 图像处理的库
import io   # python读写文件的库


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    # "referer": "http://music.163.com/song?id=167882&market=baiduqk"
    "referer": "http://music.163.com/song?id=167882"
}

stop_path = "./stopword.txt"
comment_path = "./coments.txt"


# 获取单页评论，写入文件
def get_comments(url):
    res = requests.post(url, headers=headers)
    comments_json = json.loads(res.text)
    # print(comments_json)

    if ('hotComments' in comments_json):
        comments = comments_json['hotComments']
    else:
        comments = comments_json['comments']

    # w是写，a是追加
    with open(comment_path, 'a', encoding='utf-8') as f:
        for each in comments:
            comment_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(each['time'] / 1000))
            f.write(comment_time + ' ' + each['user']['nickname'] + ':' + each['content'] + '\n')


# 请求格式
# host = "http://music.163.com/api/v1/resource/comments/R_SO_4_167882?limit=20&offset=0";
def get_all_comments():
    # 歌曲id
    id = "167882"
    page = 10
    base_url = "http://music.163.com/api/v1/resource/comments/R_SO_4_" + id + "?limit=20&offset="
    for p in range(page):
        offset = p * 20
        url = base_url + str(offset)
        get_comments(url)
        print("page " + str(p + 1) + " finish")


# 统计词频
def word_count():
    with io.open(comment_path, encoding='UTF-8') as file:
        file = file.read()
        stopwords = [line.strip() for line in open(stop_path , encoding='UTF-8').readlines()]
        words = jieba.lcut(file)
        counts = {}

        for word in words:
            if word not in stopwords:
                # 不统计字数为一的词
                if len(word) == 1:
                    continue
                else:
                    counts[word] = counts.get(word, 0) + 1

        items = list(counts.items())
        items.sort(key=lambda x: x[1], reverse=True)
        for i in range(50):
            word, count = items[i]
            print ("{:<10}{:>7}".format(word, count))


# 生成词云图
def word_cloud():
    with io.open(comment_path, encoding="utf-8") as file:
        file = file.read()
        text = ''.join(jieba.cut(file))

        mask_pic = numpy.array(Image.open("./1.jpg"))
        stopwords = open(stop_path,encoding='utf-8').read()

        # 3.设置词云的背景颜色、宽高、字数
        wordcloud = WordCloud(
            font_path='simfang.ttf',
            mask=mask_pic,
            stopwords=stopwords,
            background_color="white",
            width=1200,
            height=600,
            max_words=500
        ).generate(text)

        file_name = "./" + time.strftime("%Y%m%d%H%M%S", time.localtime()) + ".jpg"
        wordcloud.to_file(file_name)
        print("save pic finish:" + time.strftime("%Y%m%d%H%M%S", time.localtime()) + ".jpg")

        image = wordcloud.to_image()
        image.show()


def main():
    # 获取前150页评论
    get_all_comments()
    # 生成词云图
    word_cloud()
    # 统计词频
    word_count()

if __name__ == "__main__":
    main()