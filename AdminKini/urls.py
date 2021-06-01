from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.i18n import i18n_patterns
from . import view
from django.views.static import serve


urlpatterns = [
    # 基本頁面
    path('admin/', admin.site.urls),
    path('home/', view.HomePage.as_view(), name='home'),
    path('register/', view.register, name='register'),                               #註冊頁
    path('accounts/logout/', view.logout),

    # 套件接口
    path('accounts/', include('allauth.urls')),                                 #第三方登入 django-allauth
    #url(r'social-auth/', include('social_django.urls', namespace='social')),    #第三方登入social-auth-app-django
    path('oauth/', include('social_django.urls', namespace='social')),          #第三方登入social-auth-app-django
    path('i18n/', include('django.conf.urls.i18n')),                            #多語系

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

# 多語系頁面
urlpatterns += i18n_patterns(
    path('', include('Portfolio.urls')),
)