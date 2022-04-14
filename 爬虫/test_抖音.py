



import time
from collections import deque
import requests
from selenium import webdriver

# def downVideo(url, title):
#     r = requests.get(url)
#     filepath = 'video/' + title + ".mp4"
#     with open(filepath, "wb") as fp:
#         fp.write(r.content)
#     print("%s已下载"% title)


def douying():
    driver = webdriver.Chrome()
    driver.get("https://www.douyin.com/user/MS4wLjABAAAAvTIbWcK75LdlM6O666DUbmN9MK24dUlELuP3AGCcmyM4n2_yS7WsgvtS5AmRA36z")
    time.sleep(10)


if __name__ == '__main__':
    douying()
