from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import view

from .view import register, HomePage
from LineBot import views

urlpatterns = [
    # 基本頁面
    path('admin/', admin.site.urls),
    path('', HomePage.as_view(), name='home'),
    path('register/', register, name='register'),
    path('accounts/', include('allauth.urls')),
    url('social-auth/', include('social_django.urls', namespace='social')),

    # 功能頁面
    path('Vendor/', include('Vendor.urls')),
    path('Commodity/', include('Commodity.urls')),
    path('Order/', include('Order.urls')), 
    path('WechatBot/', include('WechatBot.urls')),

    # LineBot
    url('^callback', views.callback),

    # 獨立頁面
    path('Wedding/', include('Wedding.urls')),

    #path('Wedding/', WeddingPage.as_view(), name='Wedding'),

]