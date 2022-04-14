




'''
统计字符串出现的次数 并忽略大小写
'''

def get_count(str,ch):
    count = 0
    for item in s:
        if ch.upper() == item or ch.lower() == item:
            count += 1
    return count

if __name__ == '__main__':
    s = 'Heleoohheoeldjflwejfowejfl'
    ch = input('请输入要查询的字符串：')
    count = get_count(s,ch)
    print(f'{ch}出现的次数为{count}')
