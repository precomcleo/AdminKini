from django.conf.urls import url
from django.urls import path, include
from . import views    

app_name = 'VENDOR' # 新增
urlpatterns = [
    #--FBV--
    path('', views.vendor_list, name='vendor_list'),                    #店家列表
    path('<int:pk>/', views.vendor_detail, name='vendor_detail'),       #店家產品清單
    path('create/', views.re_vendor_create_view, name='vendor_create'), #新增店家
    path('<int:pk>/update/', views.vendor_update, name='vendor_update'),#更新店家資訊
    url(r'^(?P<pk>\d+)/delete/$', views.vendor_delete, name='vendor_delete'),

    #--CBV--
    #path('', views.VendorListView.as_view(), name='vendor_list'),
    #path('<int:pk>/', views.VendorDetailView.as_view(), name='vendor_detail'),
    #path('create/', views.VendorCreateView.as_view(), name='vendor_create'),
    #path('<int:pk>/update/', views.VendorUpdateView.as_view(), name='vendor_update'),
    ]