import itchat

def open_QR():
    global uuid
    uuid = itchat.get_QRuuid()
    print("itchat uuid is ============", uuid)
    qr_io = itchat.get_QR(enableCmdQR=2)
    print("qr_io",qr_io)
    qr_io.seek(0)
    print("qr_io.seek(0)",qr_io.seek(0))

    return qr_io

def auto_reply(msg):
    # friend say
    print('message：%s' %msg['Text'])
    
    ## 傳給自己:second903商店
    friendCleoId = itchat.search_friends(name='Cleo')[0]['UserName']
    if msg['ToUserName']==friendCleoId:
        print(msg['ToUserName'], friendCleoId)
        itchat.send(Job(msg['Text'], friendCleoId, 'Cleo'), toUserName=friendCleoId)

    ## 傳給Kini:Kini商店
    friendKiniId = itchat.search_friends(name='Kini')[0]['UserName']
    if msg['ToUserName']==friendKiniId:
        print(msg['ToUserName'], friendKiniId)
        itchat.send(Job(msg['Text'], friendKiniId, 'Kini'), toUserName=friendKiniId)

def Job(text, userId, userName, isWebSend=False): #-- 觸發各種事件 --#
    from ..Common import Controller
    from ..Common.Services import RateService

    print('輸入文字：%s' %text)

    # 1.翻譯
    if '翻譯' in text:
        response = Controller.Trans(text)

    # 2.商品爬蟲
    elif 'm.tb.cn' in text:
        response = Controller.Shop(text, userId, userName)
    elif '刪除' in text:
        response = Controller.DeleFile(text)
    elif '回傳' in text:
        response = Controller.SendFile(text.replace('回傳', ''))

    # 3.匯率查詢
    elif '匯率' in text:
        response = Controller.Rate(text.upper(), userId)
    elif "".join([country for country in RateService.CountryList() if country in text.upper()]):
        response = Controller.ExchangeRate(text.upper())
    
    # 4.圖靈回覆
    else :
        response = Controller.Tuling(text)

    print('輸出文字：%s' %response)
    return response    