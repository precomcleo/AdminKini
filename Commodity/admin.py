from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Item, Rate
#from django.template.loader import render_to_string
from django.utils.safestring import mark_safe 
from django.forms import TextInput, Textarea
from django.db import models


@admin.register(Item)
class ItemAdmin(ImportExportModelAdmin):
    '''--列表--'''
    # 列表的欄位寬度
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'12'})},
        models.TextField: {'widget': Textarea(attrs={'rows':3, 'cols':40})},
        models.FloatField: {'widget': TextInput(attrs={'size':'3'})},
    }
    # 列表頁顯示的欄位
    list_display = ('id', 'Url_href', 'Order_Url_href', 'Im1', 'Im2', 'Title', 'Weight', 'Weight_check', 'Price', 'Purchase_Price_check', 'Cost', 'Selling_Price')
    # 在列表允許編輯的欄位
    list_editable = 'Title', 'Purchase_Price_check', 'Weight', 'Weight_check', 'Price', 'Selling_Price'
    # 搜尋的欄位
    search_fields = ['Title']


    '''--修改頁--'''
    # 修改頁的內容
    fieldsets = (
        (None, {
            'fields': ('Title', ('Weight', 'Weight_check'),('Price', 'Purchase_Price_check'), 'Selling_Price', 'Options')
        }),
        ('URL', {
            'classes': ('collapse',),   #表示摺疊
            'fields': ('Url', 'Order_Url'),
        }),
        ('IMAGE', { #括弧內表是集中為一個欄位
            'classes': ('collapse',),   #表示摺疊
            'fields': (('Im1', 'Image1'),('Im2', 'Image2'),('Im3', 'Image3'),('Im4', 'Image4'),
                        ('Im5', 'Image5'),('Im6', 'Image6'),('Im7', 'Image7'),('Im8', 'Image8'),('Im9','Image9'), ),
        }),
    )
    # 上方顯示save紐
    save_on_top = True


    '''--方法--'''
    # 不允許編輯,這段是為了顯示縮圖所需
    readonly_fields = ('Im1', 'Im2', 'Im3', 'Im4', 'Im5', 'Im6', 'Im7', 'Im8', 'Im9')
    # 顯示ImageX的縮圖
    def Im1(self, obj):
        #return render_to_string('thumb.html', {'image': obj.Image1, 'id': '1'})
        return mark_safe('<img src="%s" height="100" width="100" />' %(obj.Image1))
    def Im2(self, obj):
        return mark_safe('<img src="%s" height="100" width="100" />' %(obj.Image2))
    def Im3(self, obj):
        return mark_safe('<img src="%s" height="100" width="100" />' %(obj.Image3))
    def Im4(self, obj):
        return mark_safe('<img src="%s" height="100" width="100" />' %(obj.Image4))
    def Im5(self, obj):
        return mark_safe('<img src="%s" height="100" width="100" />' %(obj.Image5))
    def Im6(self, obj):
        return mark_safe('<img src="%s" height="100" width="100" />' %(obj.Image6))
    def Im7(self, obj):
        return mark_safe('<img src="%s" height="100" width="100" />' %(obj.Image7))
    def Im8(self, obj):
        return mark_safe('<img src="%s" height="100" width="100" />' %(obj.Image8))
    def Im9(self, obj):
        return mark_safe('<img src="%s" height="100" width="100" />' %(obj.Image9))

@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    list_display = ('UpdateTime', 'Weight_Unit_Price', 'Exchange_Rate', 'CreditcardFee',)