



# 模拟用户登陆 只有三次机会
for i in range(1,4):
    user_name = input('请输入用户名：')
    user_pwd = input('请输入密码：')
    if user_name == 'admin' and user_pwd == '9999':
        print('登陆成功')
        break
    else:
        print('用户名或密码不正确')
        if i < 3:
            print(f'您还有{3-i}次机会')
else:
    print('对不起连续错误3次，请联系后台管理员')