#     判断支付宝数字密码是否合法


# isdigit  检测字符串是否只由数字组成
pwd = input('请输入支付宝支付密码：')

if pwd.isdigit():
    print('支付数据合法')
else:
    print('支付数字不合法，支付密码只能数数字')


print('-----------------------------------')
print('支付数据合法' if pwd.isdigit() else '支付数字不合法，支付密码只能数数字')