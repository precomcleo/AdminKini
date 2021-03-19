from django.conf.urls import url
from django.urls import path, include
from . import views

app_name = 'WEDDING'
urlpatterns = [
    path('', views.WeddingPage.as_view(), name='Wedding'),
    path('guestbook-form/', views.submitform, name='guestbook-form'),
    path('guestbook-show/', views.showform, name='guestbook-show'),
    ]