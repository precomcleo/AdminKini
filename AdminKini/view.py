from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView  
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib import messages


# 首頁
class HomePage(TemplateView):
	template_name = 'pages/home.html'

# 登出導向
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/home/')

# 註冊頁接口
def register(request):
	from django.contrib.auth.forms import UserCreationForm
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

# 範例:接口回應
def hello(request):
    return HttpResponse("Hello world ! ")

# 範例:導向頁面
def test(request):
    return render(request, 'test.html')
