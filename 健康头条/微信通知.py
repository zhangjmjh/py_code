import requests






sckey = 'SCT5835Tpjk4o7TT6Fq1OeixZ0LyDUhc'#在发送消息页面可以找到



# text为推送的title,desp为推送的描述
# url = 'https://sc.ftqq.com/%s.send?text=张健明'%sckey
url = 'https://sc.ftqq.com/%s.send?text=张健明&desp=可转债要开始挂单了'%sckey
requests.get(url)
