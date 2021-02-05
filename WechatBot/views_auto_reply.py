from django.http import JsonResponse, HttpResponse
import itchat, time, sys
from itchat.content import TEXT
import _thread


replyToGroupChat = True
functionStatus = False

def output_info(msg):
    print('[INFO] %s' % msg)

def open_QR():
    for get_count in range(10):
        output_info('Getting uuid')
        uuid = itchat.get_QRuuid()
        while uuid is None: uuid = itchat.get_QRuuid();time.sleep(1)
        output_info('Getting QR Code')
        if itchat.get_QR(uuid): break
        elif get_count >= 9:
            output_info('Failed to get QR Code, please restart the program')
            sys.exit()
    output_info('Please scan the QR Code')

    qr_io = itchat.get_QR(enableCmdQR=2)
    qr_io.seek(0)

    return qr_io
    #return uuid

def wechat_auto_reply_server(request):
    print('██wechat_auto_reply_server')
    #uuid = open_QR()
    waitForConfirm = False
    while 1:
        status = itchat.check_login()
        print(status)
        if status == '200':
            break
        elif status == '201':
            if waitForConfirm:
                output_info('Please press confirm')
                waitForConfirm = True
        elif status == '408':
            output_info('Reloading QR Code')
            uuid = open_QR()
            waitForConfirm = False
    itchat.web_init()
    itchat.show_mobile_login()
    itchat.get_friends(True)
    output_info('Login successfully')
    itchat.start_receiving()

    if status == '200':
        @itchat.msg_register(TEXT)
        def simple_reply(msg):
            print(msg['Text'])
            return 'I received: %s' % msg['Content']
        itchat.run()
        itchat.dump_login_status()
    else:
        itchat.auto_login()
        itchat.dump_login_status()
        print('Config stored, so exit.')

    return