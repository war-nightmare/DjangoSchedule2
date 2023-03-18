import os
import sys
import webbrowser
import psutil

BASE_PATH = os.path.abspath('.')
# 重复点击开始即关闭原来服务重新打开
os.system('TASKKILL /F /IM manage.exe')
def run_main():
    sys.path.append("libs")
    main = "manage.exe runserver --noreload"
    os.system(main)
    
run_main()