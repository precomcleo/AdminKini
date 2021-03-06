from django.conf.urls import url
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from . import views_auto_reply, views_schedule, views_send_url

app_name = 'WECHATBOT' # 新增
urlpatterns = [
    #AutoReply
    path('auto-reply/', views_auto_reply.auto_reply_page, name='auto-reply'),
    path('get-auto-qr/', views_auto_reply.get_auto_qr_controller, name='get-auto-qr'),
    path('bot-reply/', views_auto_reply.bot_reply_controller, name='bot-reply'),

    #Schedule
    path('schedule/', views_schedule.schedule_page, name='schedule'),
    path('set-date/', views_schedule.set_date_controller, name='set-date'),
    path('get-schedule-qr/', views_schedule.get_schedule_qr_controller, name='get-schedule-qr'),
    path('login/', views_schedule.login_controller, name='login'),

    #SendUrl
    path('send-url-page/', login_required(views_send_url.SendUrlPage.as_view()), name='send-url-page'),
    path('send-url/', views_send_url.send_url, name='send-url'),
    ]