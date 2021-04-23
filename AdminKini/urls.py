from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import view

from django.conf import settings
from django.views.static import serve
from django.urls import path, re_path

from .view import register, HomePage

urlpatterns = [
    # 基本頁面
    path('admin/', admin.site.urls),
    path('', HomePage.as_view(), name='home'),
    path('register/', register, name='register'),
    path('accounts/', include('allauth.urls')),
    url('social-auth/', include('social_django.urls', namespace='social')),

    # 功能頁面
    path('Vendor/', include('Vendor.urls')),
    path('Commodity/', include('Commodity.urls')),
    path('Order/', include('Order.urls')), 
    path('WechatBot/', include('WechatBot.urls')),
    path('UploadFile/', include('UploadFile.urls')),

    # 獨立頁面
    path('Wedding/', include('Wedding.urls')),
    re_path(r'media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),   

]