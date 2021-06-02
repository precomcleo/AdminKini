from django.conf.urls import url
from django.urls import path, include
from . import views

app_name = 'PORTFOLIO'
urlpatterns = [
    path('', views.PortfolioPage.as_view(), name='portfolio'),
    path('send-email', views.send_email, name='send-email'),
]
