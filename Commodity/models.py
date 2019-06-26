# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.html import format_html
from django.utils.safestring import mark_safe 
from datetime import date

# Create your models here.
class Item(models.Model):  
    Url = models.TextField()
    Order_Url = models.TextField(default="-", null=True, blank=True)
    Title = models.TextField()
    Weight = models.FloatField(default=0.0, null=True, blank=True)
    Weight_check = models.BooleanField(default=False, verbose_name=u'Check')
    Price = models.CharField(max_length=40)
    Purchase_Price_check = models.BooleanField(default=False, verbose_name=u'Check')
    Selling_Price = models.CharField(max_length=20, null=True, blank=True)
    Options = models.TextField(null=True, blank=True)
    Image1 = models.URLField(null=True, blank=True)
    Image2 = models.URLField(null=True, blank=True)
    Image3 = models.URLField(null=True, blank=True)
    Image4 = models.URLField(null=True, blank=True)
    Image5 = models.URLField(null=True, blank=True)
    Image6 = models.URLField(null=True, blank=True)
    Image7 = models.URLField(null=True, blank=True)
    Image8 = models.URLField(null=True, blank=True) 
    Image9 = models.URLField(null=True, blank=True)     


    def Option(self):
        options_list = str(self.Options).split(', ')
        option = ''
        option_over = ''
        read_more = ''
        for i in options_list:     
            #選項4個以內的區塊
            if options_list.index(i) <= 4: 
                option = option + (
                '<div> \
                    <font size="1" color="#888888">- %s</font> \
                </div>'
                %i)

            #選項個數超過5,顯示more按鈕
            if options_list.index(i) == 5: 
                read_more = ( 
                '<div class="flip" onclick="if(document.getElementById(\'myid_%s\').style.display==\'none\'){document.getElementById(\'myid_%s\').style.display = \'block\';}else{document.getElementById(\'myid_%s\').style.display=\'none\'}"> \
                   <span class="1">...more</span> \
                </div>'
                %(self.id, self.id, self.id))

            #選項個數超過5的區塊
            if options_list.index(i) > 4: 
                option_over = option_over + (
                '<div> \
                    <font size="1" color="#888888">- %s</font> \
                </div>'
                %i)

        #選項個數超過5,需要display外框
        option_over_display = (
        '<div class="panel" id="myid_%s" style="display:none;"> \
        %s \
        </div>' 
        %(self.id, option_over))

        #組合所有選項輸出(前4個選項＋5之後屏蔽的選項＋read_more按鈕)
        ouput = option + option_over_display + read_more
        return mark_safe('<div style="width:120px">' + ouput + '</div>')


    def Url_href(self):
        return format_html(
            '<a href="{}" target="_blank">商品連結</a>',
            self.Url) 


    def Order_href(self):
        if self.Order_Url != "-":
            return format_html(
                '<a href="{}" target="_blank">訂購連結</a>',
                self.Order_Url) 
        else:
            return "-"


    def Cost(self):
        if self.Weight == 0.0:
            return '未有重量'
        if self.Price == "需登入取Price":
            return '未有價格'

        Price = str(self.Price).replace(' ', '')

        for r in Rate.objects.raw('SELECT id, Weight_Unit_Price, Exchange_Rate, Creditcard_Fee, Transaction_Fee, PaybyCard_Fee, List_price_Rate FROM Commodity_rate'):
            if '-'in Price:
                Outt = ''
                for p in Price.split('-'):
                    Formula = str("(¥%s + %skg × ¥%s) × %s × %s%% + 成交費 + 信用卡交易費 = " %(p, self.Weight, float(r.Weight_Unit_Price), r.Exchange_Rate, r.Creditcard_Fee) )
                    In_Velue = (float(p)+ float(self.Weight)* float(r.Weight_Unit_Price))* r.Exchange_Rate * r.Creditcard_Fee
                    Velue = round(In_Velue + (In_Velue*r.Transaction_Fee) + (In_Velue*r.PaybyCard_Fee))
                    Outt = format_html(
                        '%s  \
                        <font size="1" color="#888888">%s</font>  \
                        </br>   \
                        <b>%s【×%s= %s】</b>   \
                        </br>' %(Outt, Formula, Velue, r.List_price_Rate, round(int(Velue)*r.List_price_Rate) )) 
            else:
                Formula = str("(¥%s + %skg × ¥%s) × %s × %s%% + 成交費 + 信用卡交易費 = " %(Price, self.Weight, float(r.Weight_Unit_Price), r.Exchange_Rate, r.Creditcard_Fee) )
                In_Velue = (float(Price)+ float(self.Weight)* float(r.Weight_Unit_Price))* r.Exchange_Rate * r.Creditcard_Fee
                Velue = round(In_Velue + (In_Velue*r.Transaction_Fee) + (In_Velue*r.PaybyCard_Fee))
                Outt = format_html(
                    '<font size="1" color="#888888">%s</font>  \
                    </br>   \
                    <b>%s【×%s= %s】</b>' %(Formula, Velue, r.List_price_Rate, round(int(Velue)*r.List_price_Rate) ) ) 
        return format_html('<div style="width:120px">' + Outt + '</div>') 



    def __str__(self):
        return self.Title

class Rate(models.Model):
    id = models.IntegerField(primary_key=True)
    Update_Time = models.DateField(default=date.today)
    Weight_Unit_Price = models.FloatField(default=12, null=True, blank=True, verbose_name=u'重量單價')
    Exchange_Rate = models.FloatField(default=4.6, null=True, blank=True, verbose_name=u'匯率')
    Creditcard_Fee =  models.FloatField(default=1.03, null=True, blank=True, verbose_name=u'信用卡手續費')
    Transaction_Fee =  models.FloatField(default=0.0149, null=True, blank=True, verbose_name=u'成交手續費(蝦皮)')
    PaybyCard_Fee =  models.FloatField(default=0.015, null=True, blank=True, verbose_name=u'信用卡交易手續費(蝦皮)')
    List_price_Rate = models.FloatField(default=1.3, null=True, blank=True, verbose_name=u'加成倍數')
