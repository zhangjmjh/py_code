import requests
import json
import urllib

 def getSogouImag():
    # n = length
    # cate = category
     path = 'D:/image/'

    headers = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
    url = "https://pic.sogou.com/"

    imgs = requests.get(url = url , headers = headers)
     print(imgs.text)
imgs = requests.get('http://pic.sogou.com/pics/channel/getAllRecomPicByTag.jsp?category='+cate+'&tag=%E5%85%A8%E9%83%A8&start=0&len='+str(n))

jd = json.loads(imgs.text)
    jd = jd['all_items']
    imgs_url = []
     for j in jd:
         imgs_url.append(j['bthumbUrl'])
     m = 0
    for img_url in imgs_url:
             print('***** '+str(m)+'.jpg *****'+'   Downloading...')
             urllib.request.urlretrieve(img_url,path+str(m) +'.jpg')
             m = m + 1
     print('Download complete!')

getSogouImag()

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    }
url = "https://pic.sogou.com/"

imgs = requests.get(url=url, headers=headers)
print(imgs.text)