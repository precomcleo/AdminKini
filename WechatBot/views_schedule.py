from django.shortcuts import render
import itchat, time, sys
from django.http import JsonResponse, HttpResponse
from django.shortcuts import HttpResponse, render, redirect
from .Service.scheduler_service import *
import os

wechatsend = WechatScheduler('2019-05-13 14:52:30', 'file_name', 'wechat_receive', '')

# Create your views here.
def schedule_page(request):
    context = {
        'Order':'123',
    }
    return render(request, 'wechatbot/schedule.html', context)

def set_date_controller(request):
    print('██wechat_set_date_controller')
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

def get_schedule_qr_controller(request):
    print('██wechat_get_schedule_qr_controller')
    response = {}
    response['code'] = 0
    response['message'] = 'success'
    # POST
    if request.method == 'GET':
        response['data'] = wechatsend.wechat_login_server()

    return HttpResponse(response['data'])

def login_controller(request):
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