import requests
import json
import re
import wordcloud
import jieba

def Doraemon():
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
        "Referer": "https://www.douban.com/"
    }
    # 这个循环类似于翻页操作，翻页去获取下面的评论
    for i in range(0,501,20):
        print(f'正在爬取第{i}页')
        url = f'https://movie.douban.com/subject/34913671/comments?start={i}&limit=20&status=P&sort=new_score'

        response = requests.get(url = url, headers = headers)
        response.encoding = 'utf-8'
        text = response.text

        # 解析数据，这里使用的是正则解析
        comments_list = [i for i in re.findall('<span class="short">(.*?)</span>',text,re.S)]

        # 数据存储，针对列表中每一条数据，使用open()函数，写入到txt文档中
        for comment in comments_list:
            with open(r'.\豆瓣电影影评.txt',"a",encoding="utf-8") as f:
                f.write(comment + "\n")
    print('爬取完毕')

if __name__ == '__main__':
    Doraemon()