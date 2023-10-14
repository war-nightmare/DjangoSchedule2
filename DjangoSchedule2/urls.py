"""DjangoSchedule2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from DjangoSchedule2 import settings
from django.conf.urls import static
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('show/', views.show),
    path('show/api/', views.api_show),

    path('', views.index),
    path('delete/', views.delete),
    path('add/', views.add),
    path('edit/', views.edit),

    path('index_display/', views.index_display),
    path('index_display/add/', views.add_display),
    path('index_display/edit/', views.edit_display),
    path('index_display/delete/', views.delete_display),

    path('task/list/', views.task_list),
    path('task/ajax/', views.task_ajax),

    path('index_matter/', views.index_matter),
    path('index_matter/add/', views.add_matter),
    path('index_matter/edit/', views.edit_matter),
    path('index_matter/delete/', views.delete_matter),

    path('index_attendant/', views.index_attendant),
    path('index_attendant/add/', views.add_attendant),
    path('index_attendant/edit/', views.edit_attendant),
    path('index_attendant/delete/', views.delete_attendant),

    path('settings/', views.othersettings),
    # path('update_pic/', views.update_pic),  # 上传图片
    # path('uploal_action/', views.uploal_action),  # 保存上传文件
]

urlpatterns += static.static(settings.MEDIA_URL,
                             document_root=settings.MEDIA_ROOT)

# 打包时使用
urlpatterns += static.static(settings.STATIC_URL,
                             document_root=settings.STATIC_ROOT)
