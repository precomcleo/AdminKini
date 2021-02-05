from django.shortcuts import render
import itchat, time, sys
from .Common import Controller
from .Common.Services import RateService
import os
from django.http import JsonResponse, HttpResponse
from django.shortcuts import HttpResponse, render, redirect
from .Service.WechatSchedulerService import *
from . import views_auto_reply

wechatsend = WechatScheduler('2019-05-13 14:52:30', 'file_name', 'wechat_receive', '')

# Create your views here.
def WechatBotPage(request):
    context = {
        'Order':'123',
    }
    return render(request, 'wechatbot/wechatbot_list.html', context)

def wechat_set_controller(request):
    print('██wechat_set_controller')
    response = {}
    response['code'] = 0
    response['message'] = 'success'
    # POST
    if request.method == 'POST':
        file_name = request.FILES.get('file_name')
        file_path = os.path.abspath(os.path.join("upload_dir", file_name.name))
        print(file_path)
        destination = open(file_path, 'wb+')  # 打开特定的文件进行二进制的写操作
        for chunk in file_name.chunks():  # 分块写入文件
            destination.write(chunk)
        destination.close()

        date_time = request.POST.get('date_time')
        wechat_receive = request.POST.get('group_name')
        send_message = request.POST.get('send_message')
        
        print("date_time is {0} and wechat_receive is {1} and send_message is {2}".format(date_time, wechat_receive, send_message))
        wechatsend1 = WechatScheduler(date_time, file_path, wechat_receive, send_message)
        global wechatsend
        wechatsend = wechatsend1
    return JsonResponse(response)

def wechat_send_controller(request):
    print('██wechat_send_controller')
    response = {}
    response['code'] = 0
    response['message'] = 'success'
    # POST
    if request.method == 'GET':
        response['data'] = wechatsend.wechat_login_server()

    return HttpResponse(response['data'])

def wechat_login_controller(request):
    print('██wechat_login_controller')
    # wechatsend = WechatScheduler()
    # mychat = wechatsend.mychat
    response = {}
    response['code'] = 0
    response['message'] = 'success'
    
    # POST
    if request.method == 'GET':
        # Start auto-replying
        response['data'] = wechatsend.wechat_sendfile_server()
    
    return JsonResponse(response)

def wechat_auto_reply_login_controller(request):
    print('██wechat_auto_reply_controller')
    response = {}
    response['code'] = 0
    response['message'] = 'success'
    # POST
    if request.method == 'GET':
        response['data'] = views_auto_reply.open_QR()
    
    return JsonResponse(response)