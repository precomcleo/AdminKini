from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView  
from django.contrib import auth
from django.http import HttpResponseRedirect

from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# 首頁
class HomePage(TemplateView):
	template_name = 'pages/home.html'

# 登出導向
def dologout(request):
    auth.logout(request)
    return HttpResponseRedirect('/home/')

# 註冊頁接口
def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		print("Errors", form.errors)
		if form.is_valid():
			form.save()
			return redirect('/home')
		else:
			return render(request, 'account/register.html', {'form':form})
	else:
		form = UserCreationForm()
		context = {'form': form}
		return render(request, 'account/register.html', context)

# 獲取留言表單，發送郵件給管理者
def send_email(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        #發送訊息
        send_mail(
            '%s 從 cleoliu-herou-home 發送訊息給你：%s' %(name,subject),   #信件標題
            '內容：%s, 回信至：%s, 聯絡電話：%s' %(message, email, phone),  #信件內容
            settings.EMAIL_HOST_USER,                 					#寄件信箱
            [settings.EMAIL_RECEIVE_USER],            					#收件人
            fail_silently=False
            )
        #成功回覆
        messages.success(request, '發送成功！')
        
    return render(request,'pages/home.html')

# 範例:接口回應
def hello(request):
    return HttpResponse("Hello world ! ")

# 範例:導向頁面
def test(request):
    return render(request, 'test.html')
