import re
import  requests
import xlsxwriter
import  time

def GetxxintoExcel(html):
    global count
    a = re.findall(r'"raw_title":"(.*?)"', html)
    b = re.findall(r'"view_price":"(.*?)"', html)
    c = re.findall(r'"item_loc":"(.*?)"', html)
    d = re.findall(r'"view_sales":"(.*?)"', html)
    x = []
    for i in range(len(a)):
        try:
            x.append((a[i],b[i],c[i],d[i]))
        except IndexError:
            break
    i = 0
    for i in range(len(x)):
        worksheet.write(count + i + 1, 0, x[i][0])
        worksheet.write(count + i + 1, 1, x[i][1])
        worksheet.write(count + i + 1, 2, x[i][2])
        worksheet.write(count + i + 1, 3, x[i][3])
    count = count +len(x)
    return print("已完成")


def Geturls(q, x):
    url = "https://s.taobao.com/search?q=" + q + "&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm" \
                                                 "=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306 "
    urls = []
    urls.append(url)
    if x == 1:
        return urls
    for i in range(1, x ):
        url = "https://s.taobao.com/search?q="+ q + "&commend=all&ssid=s5-e&search_type=item" \
              "&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306" \
              "&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s=" + str(
            i * 44)
        urls.append(url)
    return urls


def GetHtml(url):
    r = requests.get(url,headers =headers)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r

if __name__ == "__main__":
    count = 0
    headers = {
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
        ,"cookie":"_m_h5_tk=17316823217a5649832863301ac018c6_1616069516133; _m_h5_tk_enc=242e89d4930de9cab02afa0a3d9c8968; cookie2=22b80f77ecb843b5b86c0658c1988ab0; t=6ec12777639394f9626d45052d028270; _tb_token_=33e94e8e6e9ee; cna=GOfVGCLxY1MCAXeIVweGdn7P; xlly_s=1; _samesite_flag_=true; sgcookie=E100zUBAq2FhQPFnZAx5tofkSftBzSl4Vrp4uzgFNcwH6LhTvOgQLxxIboOuUfTlN0RmYdFAQTreqKC6C3WaElrVUw%3D%3D; unb=1997041256; uc1=cookie14=Uoe1hMSiKiE%2F6g%3D%3D&cookie16=VFC%2FuZ9az08KUQ56dCrZDlbNdA%3D%3D&existShop=false&pas=0&cookie21=W5iHLLyFeYZ1WM9hVnmS&cookie15=UIHiLt3xD8xYTw%3D%3D; uc3=vt3=F8dCuAop3lXCHLbA1dQ%3D&nk2=F5QPBBuDlGyjG3c%3D&lg2=WqG3DMC9VAQiUQ%3D%3D&id2=UojdTMFc93nGfw%3D%3D; csg=7616346e; lgc=tbzhngjianm; cookie17=UojdTMFc93nGfw%3D%3D; dnk=tbzhngjianm; skt=5c1dd4dd85dea8c4; existShop=MTYxNjA2MTI3MA%3D%3D; uc4=id4=0%40UOBZlpeenuFioU4By8hGxyF7U9mg&nk4=0%40FY5EBHcsgISlb%2FeaqsLM%2BhUJ2As6zQ%3D%3D; tracknick=tbzhngjianm; _cc_=Vq8l%2BKCLiw%3D%3D; _l_g_=Ug%3D%3D; sg=m64; _nk_=tbzhngjianm; cookie1=BdXfRiu2s4wbCIccFUPihIhIzeEZ%2BbT7R6klo9XkhBs%3D; ucn=center; tfstk=cUWNBnxX7ReaqOpbwd9qltFhVf9OZEIGmv-Ws6xn-etgmGAGihgvxkgvYnT8KCf..; isg=BJ-fo4NjAwXe3wcZAij6WHmDLvMpBPOmBc35zDHtOM6VwL5CO9CJ97HZglC-2Mse; l=eBMYWEQIji8WFaKdBO5Cnurza779mIOb8sPzaNbMiInca6M19FtR7NCQnrpwWdtjgtfmgexzPnnb5RUWP5zU-jkDBeYCPlUOr4p9-"
                }
    q = input("输入货物")
    x = int(input("你想爬取几页"))
    urls = Geturls(q,x)
    workbook = xlsxwriter.Workbook(q+".xlsx")
    worksheet = workbook.add_worksheet()
    worksheet.set_column('A:A', 70)
    worksheet.set_column('B:B', 20)
    worksheet.set_column('C:C', 20)
    worksheet.set_column('D:D', 20)
    worksheet.write('A1', '名称')
    worksheet.write('B1', '价格')
    worksheet.write('C1', '地区')
    worksheet.write('D1', '付款人数')
    xx = []
    for url in urls:
        html = GetHtml(url)
        s = GetxxintoExcel(html.text)
        time.sleep(5)
    workbook.close()


# # re库来提取信息
# a = re.findall(r'"raw_title":".*?"',html)  # 返回html中所有与raw_title有关的内容   r 后面是正则表达式语句
# b = re.findall(r'"view_price":"(.*?)"',html)
# c = re.findall(r'"item_loc":"(.*?)"',html)
# c = re.findall(r'"view_sales":"(.*?)"',html)
#
#
# # 第一个函数来获取html网页
# def gethtml(url):
#     r = requests.get(url,headers=headers)
#     r.raise_for_status()
#     r.encoding = r.apparent_encoding   #  从网页中分析网页编码的方式，这种方式比r.rncoding更加精准
#     return r
#
# 第二个获取网页的url
def geturls(q, x):  # q 表示商品名称  x 表示查几页的数据
    url = 'https://s.taobao.com/search?q=' + q +"&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm" \
                                                 "=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306 "


    if x == 1:
        return url

    for i in range(1,x):
        url = "https://s.taobao.com/search?q="+ q + "&commend=all&ssid=s5-e&search_type=item" \
              "&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306" \
              "&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s=" + str(i * 44)
        return url

# 获取商品信息并写入excel表格
def GetxxintoExcel(html):
    global count # 定义一个全局变量用户后面excel表的填写
    a = re.findall(r'"raw_title":".*?"',html)  # 返回html中所有与raw_title有关的内容   r 后面是正则表达式语句
    b = re.findall(r'"view_price":"(.*?)"',html)
    c = re.findall(r'"item_loc":"(.*?)"',html)
    d = re.findall(r'"view_sales":"(.*?)"',html)

    x = []
    for i in range(len(a)):
        try:
            x.append(a[i],b[i],c[i],d[i])
        except:
            break

    i = 0
    for i in range(len(x)):
        worksheet.write(count)


