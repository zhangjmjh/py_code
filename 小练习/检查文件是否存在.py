






import os
def CheckFile():
    print("文件夹存在:", os.path.exists('data'))
    if not os.path.exists('data'):
        # print('文件根本不存在，你再搞笑')
        os.mkdir('data')
CheckFile()