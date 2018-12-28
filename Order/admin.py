from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Inventory, Customer, Stock, OrderStatus
from django.forms import TextInput, Textarea, NumberInput
from django.db import models
# Register your models here.

class CustomerInline(admin.TabularInline): #--新增頁崁入子清單--
    model = Customer
    extra = 1#默認顯示條目的數量

class StockInline(admin.TabularInline): #--新增頁崁入子清單--
    model = Stock
    extra = 1#默認顯示條目的數量

@admin.register(Inventory)
class InventoryAdmin(ImportExportModelAdmin):
    list_display = ('id', 'Purchase_Date', 'Type', 'Weight', 'Estimated_Weight', 'shipment_Num', 'goodsname', 'specification', 'Buy','Stocks')
    list_editable = 'Purchase_Date', 'Type', 'Weight', 'Estimated_Weight', 'shipment_Num', 'goodsname', 'specification'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
    fields = ['Purchase_Date', 'Type', 'Weight', 'Estimated_Weight', 'shipment_Num', 'goodsname', 'specification', ('Buyer1', 'Buyer2', 'Buyer3', 'Buyer4', 'Buyer5'), ('Stock1', 'Stock2', 'Stock3', 'Stock4', 'Stock5')]
    # 列表的欄位寬度
    formfield_overrides = {
        models.FloatField: {'widget': TextInput(attrs={'size':'3'})},
        models.CharField: {'widget': TextInput(attrs={'size':'15'})},
    }
    inlines = (CustomerInline,StockInline)

@admin.register(Customer)
class CustomerAdmin(ImportExportModelAdmin):
    list_display = ('Inventory_id', 'Buyer')

@admin.register(Stock)
class StockAdmin(ImportExportModelAdmin):
    list_display = ('Inventory_Id', 'Stock_Name')

@admin.register(OrderStatus)
class OrderStatusAdmin(ImportExportModelAdmin):
    list_display = ('Status',)


