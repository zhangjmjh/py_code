





# 全局变量的域名

class global_var:
    app = "http://api-service-test01.shein.com"  # app测试环境
    AppVersion = '8.0.2'

def app():
    global_var.app = "app"
def app():
    return global_var.app

def AppVersion():
    global_var.AppVersion = "AppVersion"
def AppVersion():
    return global_var.AppVersion


