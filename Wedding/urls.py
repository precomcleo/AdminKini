from django.conf.urls import url
from django.urls import path, include
from . import views

app_name = 'WEDDING'
urlpatterns = [
    path('', views.WeddingPage.as_view(), name='index'),
    path('rsvp/', views.RsvpPage.as_view(), name='rsvp'),
    path('guestbook-form/', views.form, name='guestbook-form'),
    path('guestbook-board/', views.board, name='guestbook-board'),
    url(r'^(?P<pk>\d+)/delete/$', views.delete, name='guestbook-delete'),
    ]