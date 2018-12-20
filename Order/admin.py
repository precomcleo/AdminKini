from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Inventory
from django.forms import TextInput, Textarea, NumberInput
from django.db import models
# Register your models here.

@admin.register(Inventory)
class InventoryAdmin(ImportExportModelAdmin):
    list_display = ('id', 'Purchase_Date', 'Type', 'Weight', 'Estimated_Weight', 'shipment_Num', 'goodsname', 'specification', 'Buyer1', 'Buyer2', 'Buyer3', 'Buyer4', 'Buyer5', 'Stock1', 'Stock2', 'Stock3', 'Stock4', 'Stock5')
    list_editable = 'Purchase_Date', 'Type', 'Weight', 'Estimated_Weight', 'shipment_Num', 'goodsname', 'specification', 'Buyer1', 'Buyer2', 'Buyer3', 'Buyer4', 'Buyer5', 'Stock1', 'Stock2', 'Stock3', 'Stock4', 'Stock5'
    fields = ['Purchase_Date', 'Type', 'Weight', 'Estimated_Weight', 'shipment_Num', 'goodsname', 'specification', ('Buyer1', 'Buyer2', 'Buyer3', 'Buyer4', 'Buyer5'), ('Stock1', 'Stock2', 'Stock3', 'Stock4', 'Stock5')]
    # 列表的欄位寬度
    formfield_overrides = {
        models.FloatField: {'widget': TextInput(attrs={'size':'3'})},
        models.CharField: {'widget': TextInput(attrs={'size':'15'})},
    }