from django.conf.urls import url
from django.urls import path, include
from . import views   
from Order.views import shipped, order_create_view
#from .views import CustomerView

app_name = 'ORDER' # 新增
urlpatterns = [
    #--FBV--
    #url(r'^$', HomeView.as_view(), name="home"),
    path('', views.OrderPage, name='order_list'),
    path('shipped/', shipped),
    path('ordercreate/', order_create_view),
    ]