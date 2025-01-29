# 关于 DjangoSchedule2


![](https://img.shields.io/badge/python-3.9.2-3776AB.svg?logo=python) ![](https://img.shields.io/badge/django-4.2.4-092E20.svg?logo=django) ![](https://img.shields.io/badge/sqlite3-003B57.svg?logo=sqlite) ![](https://img.shields.io/badge/HTML5-E34F26.svg?logo=html5) ![](https://img.shields.io/badge/jquery-3.6.3-0769AD.svg?logo=jquery) ![](https://img.shields.io/badge/bootstrap-3.4.1-7952B3.svg?logo=bootstrap) ![](https://img.shields.io/badge/bootstrap_datetimepicker-1.9.0-brown.svg?logo=bootstrap) ![](https://img.shields.io/badge/font_awesome-4.7.0-528DD7.svg?logo=fontawesome)

DjangoSchedule2 是 DjangoSchedule 的二代版本，是一款使用 Python 开发的，针对Seewo及其教学一体机设计的，用于显示教学信息的壁纸软件。

DjangoSchedule2 使用 django 库，本地搭建服务器，客户端需使用 WallpaperEngine 等软件，粘贴网址，即可在桌面显示动态壁纸。

---

## 使用
### 开发版

```bat
python manage.py runserver <port>
```

#<port>默认为22424，下同

浏览器打开 ```127.0.0.1/<port>``` 

壁纸软件粘贴 ```127.0.0.1/<port>``` 

### 发行版

打开 ```run.exe```

浏览器自动打开 ```127.0.0.1/<port>```

壁纸软件粘贴 ```127.0.0.1/<port>```

## License

本项目使用 **MIT License** 开源。
