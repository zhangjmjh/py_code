import requests
from lxml import etree
import csv


def bajie():

    url = "https://guangdong.zbj.com/search/f/?kw=%E8%BD%AF%E4%BB%B6%E5%BC%80%E5%8F%91"
    headers = {
            "user-agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46'
        }
    response = requests.get(url=url,headers=headers)
    # print(response.text)

    # 解析
    html = etree.HTML(response.text)

    f = open('data.csv', mode='w', newline='',encoding='GBK')  # newline='':防止保存的csv文件有空行
    csv_writer = csv.writer(f)

    # 找到所有服务商的div
    div = html.xpath("/html/body/div[6]/div/div/div[3]/div[5]/div[1]/div")
    for i in div:
        name = i.xpath("./div/div/a/div[2]/div[1]/span[1]/text()")[0].strip("¥") + "元"

        title = '软件开发'.join(i.xpath("./div/div/a/div[2]/div[2]/p/text()"))

        company = i.xpath("./div/div/a[1]/div[1]/p/text()")
        #  这一步是去除了空格和换行字符
        new_company = [x.strip() for x in company if x.strip() != ''][0]

        location = i.xpath("./div/div/a[1]/div[1]/div/span/text()")[0]

        csv_writer.writerow([name, title, new_company, location])
        # print(title)

    f.close()
if __name__ == '__main__':
    bajie()