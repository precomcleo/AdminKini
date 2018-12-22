from django.conf.urls import url
from django.urls import path, include
from . import views    

app_name = 'COMMODITY' # 新增
urlpatterns = [
    #--FBV--
    path('', views.CommodityPage, name='commodity_list'),                    #店家列表
    ]