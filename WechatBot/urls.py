from django.conf.urls import url
from django.urls import path, include
from . import views, views_auto_reply
from django.views.static import serve
from django.views.generic.base import TemplateView
import os

app_name = 'WECHATBOT' # 新增
urlpatterns = [
    #AutoReply
    path('auto-reply/', views_auto_reply.auto_reply_page, name='auto-reply'),
    path('get-auto-qr/', views_auto_reply.get_auto_qr_controller, name='get-auto-qr'),
    path('bot-reply/', views_auto_reply.bot_reply_server, name='bot-reply'),

    #Schedule
    path('schedule/', views.schedule_page, name='schedule'),
    path('set-date/', views.set_date_controller, name='set-date'),
    path('get-schedule-qr/', views.get_schedule_qr_controller, name='get-schedule-qr'),
    path('login/', views.login_controller, name='login'),
    ]