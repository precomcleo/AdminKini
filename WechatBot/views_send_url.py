from django.shortcuts import render
from django.views.generic.base import TemplateView  
from .Service import send_url_service
from django.contrib.auth.decorators import login_required

class SendUrlPage(TemplateView):
	template_name = 'wechatbot/send-url-page.html'

# 顯示留言板訊息
@login_required
def send_url(request):
    # 上傳到數據庫
    if request.method == 'POST':
        text = request.POST.get('message','')

    output_messages = send_url_service.Job(text)
    # try:    
    #     output_messages = send_url_service.Job(text, isWebSend=True)
    # except:
    #     output_messages = '建檔失敗'

        
    return render(request,'wechatbot/send-url-page.html', {
        'output_messages':output_messages,
    })
