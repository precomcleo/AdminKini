# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.html import format_html
from datetime import date

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

        for r in Rate.objects.raw('SELECT id, Weight_Unit_Price, Exchange_Rate, CreditcardFee FROM Commodity_rate'):
            if '-'in Price:
                Outt = ''
                for p in Price.split('-'):
                    Formula = str("(¥%s + %skg × ¥%s) × %s × %s%% = " %(p, self.Weight, float(r.Weight_Unit_Price), r.Exchange_Rate, r.CreditcardFee) )
                    Velue = str(round((float(p)+ float(self.Weight)* float(r.Weight_Unit_Price))* r.Exchange_Rate * r.CreditcardFee))
                    Outt = format_html(
                        '%s  \
                        <font size="1" color="#888888">%s</font>  \
                        </br>   \
                        <b>%s</b>   \
                        </br>' %(Outt, Formula, Velue)) 
            else:
                Formula = str("(¥%s + %skg × ¥%s) × %s × %s%% = " %(Price, self.Weight, float(r.Weight_Unit_Price), r.Exchange_Rate, r.CreditcardFee) )
                Velue = str(round((float(Price)+ float(self.Weight)* float(r.Weight_Unit_Price))* r.Exchange_Rate * r.CreditcardFee))
                Outt = format_html(
                    '<font size="1" color="#888888">%s</font>  \
                    </br>   \
                    <b>%s</b>' %(Formula, Velue) ) 
        return Outt 



    def __str__(self):
        return self.Title

class Rate(models.Model):
    UpdateTime = models.DateField(default=date.today)
    Weight_Unit_Price = models.FloatField(default=12, null=True,blank=True)
    Exchange_Rate = models.FloatField(default=4.6, null=True,blank=True)
    CreditcardFee =  models.FloatField(default=1.03, null=True,blank=True)
