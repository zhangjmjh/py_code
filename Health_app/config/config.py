





# 全局变量的域名

class global_var:
    app = "https://zixun.001pt.com"  # app测试环境
    admin = "https://zixun-admin-v120.001pt.com"  # 后台测试环境
    versionName = '1.6.2'

def app():
    global_var.app = "app"
def app():
    return global_var.app


def admin():
    global_var.admin = "admin"
def admin():
    return global_var.admin

def versionName():
    global_var.versionName = "versionName"
def versionName():
    return global_var.versionName


