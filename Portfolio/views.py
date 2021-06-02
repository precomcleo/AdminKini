from django.shortcuts import render
from django.views.generic.base import TemplateView  

from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# Wedding頁
class PortfolioPage(TemplateView):
	template_name = 'portfolio/portfolio.html'

# 獲取留言表單，發送郵件給管理者
def send_email(request):
    if request.method == 'POST':
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        message = request.POST.get('message','')

        #發送訊息
        send_mail(
            '%s 從 cleoliu-herou-Portfolio 發送訊息給你' %name,   #信件標題
            '內容：%s, 回信至：%s' %(message, email),            #信件內容
            settings.EMAIL_HOST_USER,                           #寄件信箱
            [settings.EMAIL_RECEIVE_USER],                      #收件人
            fail_silently=False
            )
        #成功回覆
        messages.success(request, '發送成功！')

    return render(request,'portfolio/portfolio.html')