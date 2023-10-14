import os
import sys
import webbrowser
import time

BASE_PATH = os.path.abspath('.')
# 重复点击开始即关闭原来服务重新打开
os.system('TASKKILL /F /IM python.exe')
os.system('TASKKILL /F /IM manage.exe')
os.system('TASKKILL /F /IM manage.py')


def run_main():
    sys.path.append("libs")
    url = 'http://127.0.0.1:22424'
    webbrowser.open_new(url)
    main = BASE_PATH + "/manage/manage.exe runserver 22424 --noreload"
    os.system(main)


if __name__ == "__main__":
    run_main()
