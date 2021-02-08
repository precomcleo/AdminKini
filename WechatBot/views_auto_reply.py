from django.http import JsonResponse, HttpResponse
from django.shortcuts import HttpResponse, render, redirect
import itchat, time, sys
from itchat.content import TEXT
import _thread

replyToGroupChat = True
functionStatus = False
uuid = ''

def auto_reply_page(request):
    context = {
        'Order':'123',
    }
    return render(request, 'wechatbot/auto-reply.html', context)

def get_auto_qr_controller(request):
    print('██wechat_get_auto_qr_controller')
    response = {}
    response['code'] = 0
    response['message'] = 'success'
    # POST
    if request.method == 'GET':
        response['data'] = open_QR()
    
    return HttpResponse(response['data'])

def __output_info(msg):
    print('[INFO] %s' % msg)

def open_QR():
    # for get_count in range(10):
    #     __output_info('Getting uuid')
    #     uuid = itchat.get_QRuuid()
    #     while uuid is None: uuid = itchat.get_QRuuid();time.sleep(1)
    #     __output_info('Getting QR Code')
    #     if itchat.get_QR(uuid): break
    #     elif get_count >= 9:
    #         __output_info('Failed to get QR Code, please restart the program')
    #         sys.exit()
    # __output_info('Please scan the QR Code')

    global uuid
    uuid = itchat.get_QRuuid()
    print("itchat uuid is ============", uuid)
    qr_io = itchat.get_QR(enableCmdQR=2)
    print("qr_io",qr_io)
    qr_io.seek(0)
    print("qr_io.seek(0)",qr_io.seek(0))

    return qr_io
    #return uuid

def bot_reply_server(request):
    print('██wechat_bot_reply_server')
    #uuid = open_QR()
    waitForConfirm = False
    while 1:
        print(uuid)
        status = itchat.check_login(uuid)
        print(status)
        if status == '200':
            break
        elif status == '201':
            if waitForConfirm:
                __output_info('Please press confirm')
                waitForConfirm = True
        # elif status == '408':
        #     __output_info('Reloading QR Code')
        #     uuid = open_QR()
        #     waitForConfirm = False
    itchat.web_init()
    itchat.show_mobile_login()
    itchat.get_friends(True)
    __output_info('Login successfully')
    itchat.start_receiving()

    if status == '200':
        @itchat.msg_register(TEXT)
        def simple_reply(msg):
            print(msg['Text'])
            return 'I received: %s' % msg['Content']
        itchat.run(debug=True)
        itchat.dump_login_status()
    else:
        itchat.auto_login()
        itchat.dump_login_status()
        print('Config stored, so exit.')

    return