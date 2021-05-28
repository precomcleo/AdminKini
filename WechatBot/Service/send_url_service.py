from Commodity.models import Item

def Job(text): #-- 觸發各種事件 --#
    from ..Common import Controller
    from ..Common.Services import RateService

    print('輸入文字：%s' %text)

    # 1.翻譯
    if '翻譯' in text:
        result = Controller.Trans(text)
        response = '【翻譯結果】%s' %result

    # 2.商品爬蟲
    elif 'm.tb.cn' in text:
        url, title, price, options, image = Controller.ShopForWebSend(text)
        
        # 存至Commodity資料庫
        item = Item()
        item.Url = url
        item.Title = title
        item.Price =  price
        item.Options = ', '.join(options)
        try: #圖數不足則跳過
            item.Image1 = image[0]
            item.Image2 = image[1]
            item.Image3 = image[2]
            item.Image4 = image[3]
            item.Image5 = image[4]
            item.Image6 = image[5]
            item.Image7 = image[6]
            item.Image8 = image[7] 
            item.Image9 = image[8]
        except:
            pass
        item.save()

        response = '【建檔完成】%s' %title

    # 3.匯率查詢
    #elif '匯率' in text:
    #    response = Controller.Rate(text.upper(), userId)
    #elif "".join([country for country in RateService.CountryList() if country in text.upper()]):
    #    response = Controller.ExchangeRate(text.upper())
    
    # 4.圖靈回覆
    else :
        result = Controller.Tuling(text)
        response = '【回覆】%s' %result

    print('輸出文字：%s' %response)
    return response   