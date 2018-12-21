from django.contrib import admin
from .models import Vendor, Product
from django.utils.translation import gettext_lazy

class Morethanfifty(admin.SimpleListFilter): #--依照價格區間來過濾--
	title = gettext_lazy('price')
	parameter_name = 'compareprice' #/?compareprice=<%3D50
	def lookups(self, request, model_admin):
		return (
			('>50',gettext_lazy('>50')),
			('<=50',gettext_lazy('<=50')),
		)
    
	def queryset(self, request, queryset): #--定義查詢時的過濾條件--
		if self.value() == '>50':
			return queryset.filter(Product_price__gt=50)
		if self.value() == '<=50':
			return queryset.filter(Product_price__lte=50)


#admin.site.register(Product) #--簡單物件--
@admin.register(Product) #--指定顯示欄位--
class ProductAdmin(admin.ModelAdmin):
    #--顯示欄位
    #list_display = ('Product_name', 'Product_price',) #指定顯示欄位
    list_display = [field.name for field in Product._meta.fields]
    
    #--過濾 filter
    #list_filter = ('Product_price',) #指定過濾欄位
    list_filter = (Morethanfifty,)

    #--可以更改欄位
    #fields = ['Product_price'] # 顯示可以更改欄位

    #--可搜尋欄位
    search_fields = ('Product_name','Product_price')

    #--排序
    ordering = ('Product_price',) # 價格"由小到大"排序


class ProductInline(admin.TabularInline): #--新增頁崁入子清單--
    model = Product
    extra = 1#默認顯示條目的數量

#admin.site.register(Vendor) #--簡單物件--
@admin.register(Vendor) #--指定顯示欄位--
class VendorAdmin(admin.ModelAdmin):
    #--顯示欄位
    list_display = ('id', 'vendor_name', 'store_name',)
    inlines = (ProductInline,)    
    