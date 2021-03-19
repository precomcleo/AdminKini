from django.contrib import admin
from .models import UserMessage

# Register your models here.

@admin.register(UserMessage) #--指定顯示欄位--
class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in UserMessage._meta.fields]