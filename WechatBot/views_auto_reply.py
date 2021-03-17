from django.http import JsonResponse, HttpResponse
from django.shortcuts import HttpResponse, render, redirect
import itchat, time, sys
from itchat.content import TEXT
from .Service import auto_reply_service
from django.contrib.auth.decorators import login_required

uuid = ''

@login_required
def auto_reply_page(request):
    context = {
        'Order':'123',
    }
    return render(request, 'wechatbot/auto-reply.html', context)

@login_required
def get_auto_qr_controller(request):
    print('██wechat_get_auto_qr_controller')
    response = {}
    response['code'] = 0
    response['message'] = 'success'
    # POST
    if request.method == 'GET':
        response['data'] = auto_reply_service.open_QR()
    
    return HttpResponse(response['data'])

@login_required
def bot_reply_controller(request):
    global uuid
    print('██wechat_bot_reply_server')
    waitForConfirm = False
    while 1:
        print(uuid)
        status = itchat.check_login(uuid)
        print(status)
        if status == '200':
            break
        elif status == '201':
            if waitForConfirm:
                print('[INFO] Please press confirm')
                waitForConfirm = True
        elif status == '408':
            print('[INFO] Reloading QR Code')
            uuid = auto_reply_service.open_QR()
            waitForConfirm = False

    itchat.web_init()
    itchat.show_mobile_login()
    itchat.get_friends(True)
    print('[INFO] Login successfully')
    itchat.start_receiving()

    if status == '200':
        @itchat.msg_register(TEXT)
        def simple_reply(msg):
            auto_reply_service.auto_reply(msg)
        itchat.run(debug=True)
        itchat.dump_login_status()
    else:
        itchat.auto_login()
        itchat.dump_login_status()
        print('Config stored, so exit.')

    return

    

    
