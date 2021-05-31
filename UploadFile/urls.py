from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'UPLOADFILE'
urlpatterns = [
    # 相片牆
    path('', views.index, name='index'), # 列表
    #path('download/<id>', views.download, name='download'),  # 下載
    #path('delete/<id>', views.delete, name='delete'),  # 刪除

    # 上傳下載檔案
    path('upload-file', views.upload_file , name='upload_file'), # 上傳檔案
    path('download-file/<name>', views.download_file, name='download_file') # 下載檔案
]
