
# -*- coding: utf-8 -*-
# @file     : 登录后台-肖.py
# @Time     : 2021-06-16-0016 10:45
# @Author   : xiao_ning_hui
# @software : PyCharm
import os
import json
import requests
import base64
import time
import datetime
import pyautogui,pyperclip
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

class Login():
    login_url = "https://zixun-admin-v120.001pt.com/#/login"
    phone = "zhangjm"
    password = "123456"
    driver = webdriver.Chrome()
    driver.get(login_url)
    # driver.maximize_window()
    # 指定图片名称和保存路径
    pic_path = "D:\\pic_code\\pic_code_{}.jpg".format(datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))
    pyperclip.copy(pic_path)

    def save_code(self):
        #验证码元素
        code_pic = self.driver.find_element_by_class_name("check-code")
        #鼠标移动至验证码图片处
        action = ActionChains(self.driver).move_to_element(code_pic)

        #右键验证码保存图片然后回车
        action.context_click(code_pic)
        action.perform()
        pyautogui.typewrite(["v"])

        #粘贴指定的图片名和路径
        time.sleep(1)
        pyautogui.hotkey("ctrlleft","v")
        pyautogui.typewrite(["enter"])
        time.sleep(1)

    def get_code(self):
        try:
            with open(self.pic_path, 'rb')as file:
                pic_base64 = base64.b64encode(file.read())
                data = pic_base64.decode()
                file.close()
            response = requests.post("http://192.168.123.156:5050/code",data = {"imgcode":data})
            json_data = json.loads(response.text)
            code = json_data["msg"]
            return code
        except:
            print("获取验证码失败")

    def admin_login(self):
        self.driver.find_element_by_xpath("//input[@placeholder='帐号']").send_keys(self.phone)
        self.driver.find_element_by_xpath("//input[@placeholder='密码']").send_keys(self.password)
        self.driver.find_element_by_xpath("//input[@placeholder='验证码']").send_keys(self.get_code())
        self.driver.find_element_by_xpath('//button[@type="button"]').click()
        try:
            login_info = WebDriverWait(self.driver,5).until(lambda driver: self.driver.find_element_by_xpath("//div[@class='login-out-btn']")).text
            if login_info == "退出登录":
                print("登录成功")
        except:
            print("登录失败")
            self.driver.quit()

    def ad_page(self):
        pass

if __name__ == '__main__':
        login = Login()
        login.save_code()
        login.get_code()
        login.admin_login()










#获取验证码图片url
# pic_url = driver.find_element_by_class_name("check-code").get_attribute("src")
# print(pic_url)
