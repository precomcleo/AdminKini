from django.contrib import admin
from .models import Photo

# Register your models here.

@admin.register(Photo) #--指定顯示欄位--
class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Photo._meta.fields]