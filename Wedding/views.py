from django.shortcuts import render
from django.views.generic.base import TemplateView  
from Wedding.models import UserMessage
import random

# Wedding頁
class WeddingPage(TemplateView):
	template_name = 'wedding/wedding.html'

class CardPage(TemplateView):
	template_name = 'wedding/card.html'

class RsvpPage(TemplateView):
	template_name = 'wedding/rsvp.html'

# 獲取留言表單，填入留言信息並存儲到數據庫中
def form(request):
    return render(request,'wedding/guestbook-form.html')

# 顯示留言板訊息
def board(request):
    # 上傳到數據庫
    if request.method == 'POST':
        usermessage = UserMessage()
        usermessage.name = request.POST.get('name','')
        usermessage.email = request.POST.get('email','')
        usermessage.message = request.POST.get('message','')
        usermessage.object_id = str(random.randint(0,10000)).zfill(5) # 自动补零
        usermessage.save()
    # 取出當前數據庫中所有記錄，並傳入到下一個html中
    all_messages = UserMessage.objects.all()
    return render(request,'wedding/guestbook-board.html', {
        'all_messages':all_messages,
    })

from django.http import HttpResponseForbidden
from django.views.decorators.http import require_http_methods #這個 view 可以接收的 HTTP methods
from django.contrib.auth.decorators import login_required #只有已登入使用者才能進入這個 view
from django.http import HttpResponse
from django.shortcuts import redirect
from django.http import Http404

@login_required
def delete(request, pk):
    userMessage = UserMessage.objects.get(pk=pk)
    userMessage.delete()

    return redirect('/Wedding/guestbook-board')