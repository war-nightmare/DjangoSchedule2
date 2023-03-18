@echo off
if "%1"=="h" goto begin
start mshta vbscript:createobject("wscript.shell").run("""%~nx0"" h",0)(window.close)&&exit
:begin
TASKKILL /F /IM manage.exe
start http://127.0.0.1:8000/
manage.exe runserver --noreload