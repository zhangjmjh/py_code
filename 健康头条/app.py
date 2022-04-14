import os
import shutil
import time
import datetime
import json
import requests
from bs4 import BeautifulSoup

class Monitor:
    headers = {'content-type': 'application/json'}
    webhook = "https://oapi.dingtalk.com/robot/send?access_token=edb8ee35cb109ea485470450de746388cf510311df28fc8c3e4a15ffd8855490"  #  测试环境
    html_path = 'D:\\test_app\\report\\html\\'
    jtl_path = 'D:\\test_app\\report\\jtl\\'
    his_path = 'D:\\test_app\\report\\his_report\\'
    jmx_path = 'D:\\test_app'

    def run_file(self):

        # 1、删除 html 报告
        os.chdir(self.html_path)   # 相当于 cd的命令 切换到这个目录下
        html = os.listdir(self.html_path)  # os.listdir返回的是括号里包含的文件，通常用来提取其中的文件，用来循环遍历 ['TestReport.html']
        # print(html)  #['TestReport.html']
        if len(html) > 0:
            for i in html:
                os.remove(i)

        # 2、删除 jtl 报告
        os.chdir(self.jtl_path)
        jtl = os.listdir(self.jtl_path)
        if len(jtl) > 0:
            for j in jtl:
                os.remove(j)

        # 3、开始运行脚本
        os.chdir(self.jmx_path)
        print('开始运行脚本')
        os.system("ant")
        print('脚本运行结束')

        # 4、复制文件到his_report
        # time_str = datetime.datetime.now().strftime('%Y%m%d %H-%M-')
        time_str = time.strftime("%Y%m%d-%H-%M-",time.localtime())  #  这里要特别注意 win系统的文件名不支持:号 不能把时间格式那里含有:号  但是linux系统是支持的
        print(time_str)
        os.chdir(self.html_path)
        file = os.listdir(self.html_path)
        if len(file) > 0:
            # 复制旧文件到新文件夹中
            shutil.copyfile(self.html_path + "TestReport.html",self.his_path + time_str + "TestReport.html")

        # 5、找出错误数，并发送钉钉通知
        with open('TestReport.html','r',encoding='utf-8') as wb_data:
            soup = BeautifulSoup(wb_data,'lxml')  # 解析网页中的元素
            # print(Soup);  #  解析出网站的html代码
            failureNum = soup.select("#failureNum")[0].get_text()
            num = int(failureNum)
            if num > 0:
                data = {
                    "msgtype":"text",
                    "text":{'content':'业务报警'+f"接口监控报错！\n异常接口数：{num}\n报告名称："+time_str+"TestReport.html\n报告查看路径：http://192.168.123.156:8091/"+time_str+"TestReport.html".format(num=num)}
                }
                res = requests.post(url=self.webhook,data=json.dumps(data),headers=self.headers)
                print(res.text)
        self.find_slow_interface(soup)


    # 找出接口响应时间大于3s的接口，并放到一个txt文件里面
    def find_slow_interface(self, soup):
        responseTime_List = soup.select("#responseTime")
        responseName_List = soup.select("#responseName")
        interface_list = soup.select("#interface")
        interface_set = []
        response_file = open(self.html_path + '\\response_time.txt', 'w', encoding="utf-8")
        for i ,j ,k in zip(responseTime_List, responseName_List, interface_list):
                end = i.get_text().index(' ')  # 找出空格的位置1
                response_time = i.get_text()[0: end]  # 指明取值范围从从0开始到后面的空格结束
                interface = j.get_text()
                response_name = k.get_text()

                if int(response_time) > 5000 and interface not in interface_set:
                    interface_set.append(interface)
                    response_file.write("接口名称:{response_name},{interface}          {response_time}ms".format(response_name=response_name,interface=interface,response_time=response_time)+'\n')
                    print(response_time)
        response_file.close()

        # 有请求时间超过3s的接口被写入文件后发送钉钉通知
        time_str = time.strftime("%Y%m%d-%H-%M-",time.localtime())
        size = os.path.getsize('D:\\test_app\\report\\html\\response_time.txt')
        # print(size)
        if size == 0:
            print('没有超过3s的接口')

        else:
            data = {
                "msgtype": "text",
                "text": {
                    'content': '业务报警：' + '有接口请求时间大于5s'+"\n"
                    '报告查看路径：http://192.168.123.156:8091/'+time_str+"TestReport.html"}
            }
            ret = requests.post(url=self.webhook, data=json.dumps(data), headers=self.headers)

if __name__ == '__main__':
    m = Monitor()
    m.run_file()

