# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.html import format_html
from django.utils.safestring import mark_safe 
from datetime import date
from Commodity.common import Expand

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
        ouput = Expand.OptionMoreBlock(self, options_list, 4)
        return mark_safe('<div style="width:120px">' + ouput + '</div>')

    def Url_href(self):
        return format_html('<a href="{}" target="_blank">商品連結</a>',self.Url)

    def Order_href(self):
        if self.Order_Url != "-":
            return format_html('<a href="{}" target="_blank">訂購連結</a>',self.Order_Url) 
        else:
            return "-"

    def Cost(self):
        rate_detail = Rate.objects.raw('SELECT id, Weight_Unit_Price, Exchange_Rate, Creditcard_Fee, Transaction_Fee, PaybyCard_Fee, List_price_Rate FROM Commodity_rate')
        ouput = Expand.PriceMoreBlock(self, rate_detail)
        return mark_safe('<div style="width:120px">' + ouput + '</div>') 

    def __str__(self):
        return self.Title


class Rate(models.Model):
    id = models.IntegerField(primary_key=True)
    Update_Time = models.DateField(default=date.today)
    Weight_Unit_Price = models.FloatField(default=13.8, null=True, blank=True, verbose_name=u'重量單價/1kg')
    Exchange_Rate = models.FloatField(default=4.6, null=True, blank=True, verbose_name=u'匯率')
    Creditcard_Fee =  models.FloatField(default=1.03, null=True, blank=True, verbose_name=u'信用卡手續費')
    Transaction_Fee =  models.FloatField(default=0.0149, null=True, blank=True, verbose_name=u'成交手續費(蝦皮)')
    PaybyCard_Fee =  models.FloatField(default=0.015, null=True, blank=True, verbose_name=u'信用卡交易手續費(蝦皮)')
    List_price_Rate = models.FloatField(default=1.3, null=True, blank=True, verbose_name=u'加成倍數')
