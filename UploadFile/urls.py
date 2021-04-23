from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'UPLOADFILE'
urlpatterns = [
    path('', views.index, name='Index'), # 列表
    #path('download/<id>', views.download, name='download'),  # 下載
    #path('delete/<id>', views.delete, name='delete'),  # 刪除
]
