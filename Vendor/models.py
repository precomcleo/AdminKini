from django.db import models
from django.contrib import admin
from django.urls import reverse
from django.conf import settings

# Create your models here.
class Vendor(models.Model):
    vendor_name = models.CharField(max_length = 20)    #供應商名稱
    store_name = models.CharField(max_length = 10)     #供應店家名稱
    phone_number = models.CharField(max_length = 20)   #店家電話號碼
    address = models.CharField(max_length = 100)       #店家地址
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, related_name='owned_stores', on_delete=models.CASCADE)

    # 覆寫 __str__
    def __str__(self):
        return self.vendor_name

    def can_user_delete(self, user): #--判斷owner--
        if not self.owner or self.owner == user:
            return True
        if user.has_perm('stores.delete_store'):
            return True
        return False
    
    def get_absolute_url(self): #--pk關聯--
        return reverse('VENDOR:vendor_detail', kwargs={'pk': self.pk})
                     
class Product(models.Model):
    Product_name = models.CharField(max_length = 30)                      #產品名稱
    Product_price = models.DecimalField(max_digits = 3, decimal_places=0) #產品價錢               
    Product_vendor = models.ForeignKey('Vendor', related_name='Product_menu_items', on_delete=models.CASCADE)  #產品供應商
#ForeignKey 對應到 Vendor 類別，on_delete 是當對應的類別被刪除之後，對應到別人的資料就要刪除（CASCADE）（一個攤販收店了，就也再也吃不到它賣的每一樣食物了） 

    def __str__(self):
        return self.Product_name

class VendorAdmin(admin.ModelAdmin):
	list_display = ('id', 'vendor_name') 