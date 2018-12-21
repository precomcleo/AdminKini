# -*- coding: utf-8 -*-
 
#from django.http import HttpResponse
# from django.shortcuts import render
 
# def hello(request):
#     context          = {}
#     context['hello'] = 'Hello World!'
#     return render(request, 'hello.html', context)

from django.http import HttpResponse
from django.shortcuts import render, redirect
   
def hello(request):
    return HttpResponse("Hello world ! ")

def test(request):
    return render(request, 'test.html')

from django.contrib.auth.forms import UserCreationForm # 新增
def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		print("Errors", form.errors)
		if form.is_valid():
			form.save()
			return redirect('/')
		else:
			return render(request, 'registration/register.html', {'form':form})
	else:
		form = UserCreationForm()
		context = {'form': form}
		return render(request, 'registration/register.html', context)

from django.views.generic.base import TemplateView
class HomePage(TemplateView):
	template_name = 'pages/home.html'


# def rest_get(request):
#     return render(request, 'index.html')
# def add(request):
#     a = request.GET['a']
#     b = request.GET['b']
#     a = int(a)
#     b = int(b)
#     return HttpResponse(str(a+b))

# from .forms import AddForm
# def rest_post(request):
#     if request.method == 'POST':# 当提交表单时
#         form = AddForm(request.POST) # form 包含提交的数据
#         if form.is_valid():# 如果提交的数据合法
#             a = form.cleaned_data['a']
#             b = form.cleaned_data['b']
#             return HttpResponse(str(int(a) + int(b)))
#     else:# 当正常访问时
#         form = AddForm()
#     return render(request, 'index.html', {'form': form})