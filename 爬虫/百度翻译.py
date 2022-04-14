
import requests
import json

def Baidu():
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
    }
    url = 'https://fanyi.baidu.com/sug'
    data = {
        'kw' : 'dog'
    }
    response = requests.post(url=url, headers=headers, data=data)
    page_text = response.json()  #  响应的数据里面是json()形式的就用这个方法，记住要导包
    print(page_text)

    fp = open('./Baidufanyi.json', 'w' , encoding='utf=8')
    json.dump(page_text, fp=fp, ensure_ascii=False)
    # json.dump  将一个python类型的数据结构比如字典，转换成一个JSON
    # json.loads  将一个JSON编码的字符串转换回一个Python数据结构


if __name__ == '__main__':
    Baidu()
