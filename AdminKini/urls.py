"""AdminKini URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from . import view
from .view import HomePage, register
from LineBot import views

from django.conf.urls.static import static
from . import settings

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage.as_view(), name='home'),
    path('accounts/', include('allauth.urls')),
    url(r'social-auth/', include('social_django.urls', namespace='social')),
    path('register/', register, name='register'),

    path('Vendor/', include('Vendor.urls')),
    path('Commodity/', include('Commodity.urls')),
    path('Order/', include('Order.urls')), 
    path('WechatBot/', include('WechatBot.urls')),

    url('^callback', views.callback),
]