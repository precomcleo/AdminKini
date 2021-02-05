from django.conf.urls import url
from django.urls import path, include
from . import views, views_auto_reply
from django.views.static import serve
from django.views.generic.base import TemplateView
import os

app_name = 'WECHATBOT' # 新增
urlpatterns = [
    #--FBV--
    path('', views.WechatBotPage, name='index'),
    #path('', TemplateView.as_view(template_name='wechatbot_list.html')),
    path('auroSend/', views.wechat_auto_reply_login_controller, name='send'),
    path('botReply/', views_auto_reply.wechat_auto_reply_server, name='openQR'),

    #AutoReply
    path('setdate/', views.wechat_set_controller, name='setdate'),
    path('send/', views.wechat_send_controller, name='send'),
    path('login/', views.wechat_login_controller, name='login'),
    ]