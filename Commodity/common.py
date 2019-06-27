from django.utils.safestring import mark_safe 

class Expand():
    #--多顏多尺區塊--
    def OptionMoreBlock(self, optionList, overNum):
        option_start = ''
        option_over = ''
        read_more = ''
        for i in optionList:     
            #選項overNum個以內的區塊
            if optionList.index(i) <= overNum: 
                option_start = option_start + (
                '<div> \
                    <font size="1" color="#888888">- %s</font> \
                </div>'
                %i)

            #選項個數超過overNum,顯示more按鈕
            if optionList.index(i) == overNum + 1: 
                read_more = ( 
                '<div class="flip" onclick="if(document.getElementById(\'optionId_%s\').style.display==\'none\'){document.getElementById(\'optionId_%s\').style.display = \'block\';}else{document.getElementById(\'optionId_%s\').style.display=\'none\'}"> \
                    <span class="1">...more</span> \
                </div>'
                %(self.id, self.id, self.id))

            #選項個數超過overNum的區塊
            if optionList.index(i) > overNum: 
                option_over = option_over + (
                '<div> \
                    <font size="1" color="#888888">- %s</font> \
                </div>'
                %i)

        #選項個數超過overNum,需要display外框
        option_over_display = (
        '<div class="panel" id="optionId_%s" style="display:none;"> \
        %s \
        </div>' 
        %(self.id, option_over))

        #組合所有選項輸出(前overNum個選項＋overNum之後屏蔽的選項＋read_more按鈕)
        ouput = option_start + option_over_display + read_more
        return ouput


    #--進貨價區塊--
    def PriceMoreBlock(self, rate_detail):
        if self.Weight == 0.0:
            return '未有重量'
        if self.Price == "需登入取Price":
            return '未有價格'

        Price = str(self.Price).replace(' ', '')
        for r in rate_detail:
            #多段進價
            if '-'in Price:
                Outt = ''
                Outt_over = ''
                read_more = ''
                price_list = Price.split('-')
                for p in Price.split('-'):
                    #              (售價 + 重量*重量單價) * 匯率 * 信用卡手續費 + 成交費 + 信用卡交易費 
                    Formula = str("(¥%s + %skg × ¥%s) × %s × %s%% + 成交費 + 信用卡交易費 = " %(p, self.Weight, float(r.Weight_Unit_Price), r.Exchange_Rate, r.Creditcard_Fee) )
                    In_Velue = (float(p)+ float(self.Weight)* float(r.Weight_Unit_Price))* r.Exchange_Rate * r.Creditcard_Fee
                    Velue = round(In_Velue + (In_Velue*r.Transaction_Fee) + (In_Velue*r.PaybyCard_Fee))
                    
                    #多段進價2個以內的區塊
                    if price_list.index(p) <= 1: 
                        Outt = Outt + (
                            '<font size="1" color="#888888">%s</font>  \
                            </br>   \
                            <b>%s【×%s= %s】</b>   \
                            </br>' %(Formula, Velue, r.List_price_Rate, round(int(Velue)*r.List_price_Rate) )) 

                    #多段進價個數超過2,顯示more按鈕
                    if price_list.index(p) == 2: 
                        read_more = ( 
                        '<div class="flip" onclick="if(document.getElementById(\'price_%s\').style.display==\'none\'){document.getElementById(\'price_%s\').style.display = \'block\';}else{document.getElementById(\'price_%s\').style.display=\'none\'}"> \
                        <span class="1">...more</span> \
                        </div>'
                        %(self.id, self.id, self.id))

                    #多段進價個數超過2的區塊
                    if price_list.index(p) > 1: 
                        Outt_over = Outt_over + (
                            '<font size="1" color="#888888">%s</font>  \
                            </br>   \
                            <b>%s【×%s= %s】</b>   \
                            </br>' %(Formula, Velue, r.List_price_Rate, round(int(Velue)*r.List_price_Rate) )) 

                #多段進價個數超過2,需要display外框
                Outt_over_display = (
                '<div class="panel" id="price_%s" style="display:none;"> \
                %s \
                </div>' 
                %(self.id, Outt_over))

                #組合所有多段進價輸出(前2個選項＋2之後屏蔽的選項＋read_more按鈕)
                Outt = Outt + Outt_over_display + read_more

            #單一近價
            else:
                Formula = str("(¥%s + %skg × ¥%s) × %s × %s%% + 成交費 + 信用卡交易費 = " %(Price, self.Weight, float(r.Weight_Unit_Price), r.Exchange_Rate, r.Creditcard_Fee) )
                In_Velue = (float(Price)+ float(self.Weight)* float(r.Weight_Unit_Price))* r.Exchange_Rate * r.Creditcard_Fee
                Velue = round(In_Velue + (In_Velue*r.Transaction_Fee) + (In_Velue*r.PaybyCard_Fee))
                Outt = mark_safe(
                    '<font size="1" color="#888888">%s</font>  \
                    </br>   \
                    <b>%s【×%s= %s】</b>' %(Formula, Velue, r.List_price_Rate, round(int(Velue)*r.List_price_Rate) ) ) 

        return Outt