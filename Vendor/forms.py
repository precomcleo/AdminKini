from django import forms
from django.utils.translation import gettext_lazy as _# 新增

from .models import Vendor, Product

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = '__all__'
        # 新增 labels 對應
        labels = {
            'vendor_name': _('廠商名稱'),
            'store_name' : _('店名'),
            'phone_number' : _('電話'),
            'address' : _('地址'),
        }

class VendorModelForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = '__all__'
            # fields = (
            #         'vendor_name',
            #         'store_name',
            #         'phone_number',
            #         'address',
            # )
        labels = {
            'vendor_name': _('攤販名稱'),
            'store_name' : _('店名'),
            'phone_number' : _('電話'),
            'address' : _('地址'),
        }