import requests
from pyquery import PyQuery as pq



headers={
    'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56"
}

def request_html(q):
    url='http://dict.youdao.com/search?q={}&keyfrom=new-fanyi.smartResult'.format(q)
    try:
        response=requests.get(url,headers).text
        return response
    except Exception:
        print('request error')


def The_dictionary(html):
    doc=pq(html)
    data=doc('#phrsListTab').items()

    for i in data:
        print(i.find('.trans-container').text())

    The_phrase_phrase=input('是否查询此单词的短语(1.是,2，不是):')

    if The_phrase_phrase == '1':
        phrase=doc('#wordGroup').items()
        for p in phrase:
            print(p.find('.wordGroup').text())

a=input('要查询的单词:')
The_dictionary(request_html(a))
