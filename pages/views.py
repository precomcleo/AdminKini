from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'pages/home.html') #render 會負責處理 template，產生一個合法的 HTML 檔案，並依此建立 HTTP response
