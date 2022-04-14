



import pyautogui as pg   # 可以控制键盘、鼠标的库。我们可以利用它实现自动发消息
import pyperclip as pc   # 可以将文本复制到剪贴板
from apscheduler.schedulers.blocking import BlockingScheduler   # 可以创建定时任务

# 操作间隔为1秒
pg.PAUSE = 1

name = '周嘉颖'
msg = '你真好看'

def main():
	# 打开微信
	pg.hotkey('alt', 'z')  # 启动微信
	pg.hotkey('ctrl', 'f')  # 查找

	# 找到联系人
	pc.copy(name)
	pg.hotkey('ctrl', 'v')  # 粘贴消息
	pg.press('enter')

	# 发送消息
	pc.copy(msg)
	pg.hotkey('ctrl', 'v')
	pg.press('enter')

	# 隐藏微信
	pg.hotkey('alt', 'z')

if __name__ == '__main__':
	scheduler = BlockingScheduler() # 实例化一个调度器
	# scheduler.add_job(main, 'cron', hour=14, minute=53) # 添加任务 表示每天 14点53分 发消息
	scheduler.add_job(main, 'interval', seconds=3) # 添加任务 表示每隔 3s 发消息
	scheduler.start()
