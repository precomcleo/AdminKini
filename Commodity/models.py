# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.html import format_html


# Create your models here.
class Item(models.Model):  
    Url = models.TextField()
    Title = models.TextField()
    Weight = models.FloatField(default=0.0, null=True,blank=True)
    Weight_check = models.BooleanField(default=False, verbose_name=u'估重')
    Price = models.CharField(max_length=15)
    Purchase_Price_check = models.BooleanField(default=False, verbose_name=u'確認')
    Selling_Price = models.CharField(max_length=15, null=True,blank=True)
    Options = models.TextField(null=True,blank=True)
    Image1 = models.URLField(null=True,blank=True)
    Image2 = models.URLField(null=True,blank=True)
    Image3 = models.URLField(null=True,blank=True)
    Image4 = models.URLField(null=True,blank=True)
    Image5 = models.URLField(null=True,blank=True)
    Image6 = models.URLField(null=True,blank=True)
    Image7 = models.URLField(null=True,blank=True)
    Image8 = models.URLField(null=True,blank=True) 
    Image9 = models.URLField(null=True,blank=True) 
    


    def Url_href(self):
        return format_html(
            '<a href="{}" target="_blank">商品連結</a>',
            self.Url) 

    def Cost(self):
        if self.Weight == 0.0:
            return '未有重量'
        Price = str(self.Price).replace(' ', '')
        if '-'in Price:
            Purchase = Price.split('-')[0]
        cost = (float(Purchase)+ float(self.Weight)*11.5)*4.531 *1.03 #(批價+重量*公斤/元)*匯率*信用卡手續費 (4.5=匯率;11.5=公斤/元)
        return round(cost)



    def __str__(self):
        return self.Title
