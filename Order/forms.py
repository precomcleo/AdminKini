from django import forms
from django.utils.translation import gettext_lazy as _# 新增

from .models import Customer, Inventory

class CustomerForm(forms.ModelForm):    
    class Meta:
        model = Customer
        fields = ('Buyer',)

class InventoryForm(forms.ModelForm):    
    class Meta:
        model = Inventory
        fields = ('Purchase_Date', 'Type', 'goodsname', 'specification',)#'__all__'
        labels = {
            'Purchase_Date': _('日期'),
            'Type' : _('來源'),
            'goodsname' : _('品項'),
            'specification' : _('規格'),
        }