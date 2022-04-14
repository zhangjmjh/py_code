
# 爬取豆瓣Top250电影

from bs4 import BeautifulSoup
import re
import urllib.request, urllib.error
import xlwt
import sqlite3

# 电影详情链接，图片链接，影片中文名，影片外国名，评分，评价数，概况，相关信息
findTitle = re.compile(r'<span class="title">(.*?)</span>')  # 影片中文名
findLink = re.compile(r'<a href="(.*?)">')  # 电影详情链接
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')   # 评分
findJudge = re.compile(r'<span>(.*?)人评价</span>')   # 评价人数
findBd = re.compile(r'<span class="inq">(.*?)</span>', re.S)    #  相关信息 re.S 将字符串看作一个整体


def main():
    baseurl = 'https://movie.douban.com/top250?start='
    savepath = "豆瓣电影Top250.xls"
    datalist = getData(baseurl)
    saveDate(datalist,savepath)

def askURL(url):
    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"}
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    html = response.read().decode("utf-8")
    return html

def getData(baseurl):
    datalist = []
    for i in range(0, 10):
        url = baseurl + str (i * 25)
        html = askURL(url)  # 保存获取到的网页源码
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all("div",class_="item"):
            data = []
            item = str(item)

            link = re.findall(findLink, item)[0]
            data.append(link)

            title = re.findall(findTitle, item)[0]
            data.append(title)

            rating = re.findall(findRating, item)[0]
            data.append(rating)

            judge = re.findall(findJudge, item)[0]
            data.append(judge)

            if bd:
                bd = re.findall(findBd, item)[0]
            else:
                bd = ''
            print(bd)
            # bd = re.sub('<br/>', " ", bd)
            # bd = re.sub('/', " ", bd)
            # data.append(bd.strip())    # strip()   去除首尾空格
            datalist.append(bd)
    return datalist

def saveDate(datalist,savepath):
    book = xlwt.Workbook(encoding='utf-8',style_compression=0)   # 常见workbook对象
    sheet = book.add_sheet('豆瓣电影Top250', cell_overwrite_ok=True)  #  创建工作表
    col = ('影片中文名','电影详情链接','评分','评价人数','相关信息')
    for i in range(0,5):
        sheet.write(0,i,col[i])  # 列名
    for i in range(0,250):
        data = datalist[i]
        for j in range(0,5):
            sheet.write(i+1,j,data[j])  # 数据
    book.save(savepath) # 保存

if __name__ == '__main__':
    main()
    print('爬取完毕')

