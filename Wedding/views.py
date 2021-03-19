from django.shortcuts import render
from django.views.generic.base import TemplateView  
from Wedding.models import UserMessage
import random

# Wedding頁
class WeddingPage(TemplateView):
	template_name = 'wedding/wedding.html'

class RsvpPage(TemplateView):
	template_name = 'wedding/rsvp.html'

# 獲取留言表單，填入留言信息並存儲到數據庫中
def submitform(request):
    return render(request,'wedding/guestbook-form.html')

# 顯示留言板訊息
def showform(request):
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