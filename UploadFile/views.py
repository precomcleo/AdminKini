import os
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.http import FileResponse
from django.utils.http import urlquote
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import UploadModelForm, FileForm
from UploadFile.models import Photo, File

@login_required
def index(request):
    photos = Photo.objects.all()  #查詢所有資料
    form = UploadModelForm()

    if request.method == "POST":
        form = UploadModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/UploadFile/')
    
    context = {
        'photos': photos,
        'form': form
    }
    return render(request, 'uploadfile/upload-photo.html', context)

# # 下載文件
# def download(request, id):
#     file_info = IMG.objects.get(id=id)
#     print('下載的文件名：' + file_info.file_name)
#     file = open(file_info.file_path, 'rb')
#     response = FileResponse(file)
#     response['Content-Disposition'] = 'attachment;filename="%s"' % urlquote(file_info.file_name)
#     return response

# # 刪除文件
# def delete(request, id):
#     file_info = IMG.objects.get(id=id)
#     file_info.delete()
#     file_infos = IMG.objects.all()
#     return HttpResponseRedirect('/UploadFile/list')

# 上傳檔案
@login_required
def upload_file(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            # 選擇的檔案
            files = request.FILES.getlist('file')

            # 遍歷寫入到資料庫中
            for file in files:
                #判斷是否已有檔案
                if File.objects.filter(name=file.name).exists():
                    messages.error(request, '[%s] 檔案已存在!' %file.name) 
                else: 
                    # 寫入到資料庫中
                    file_model = File(name=file.name, path=os.path.join('./media/upload', file.name))
                    file_model.save()
                    # 寫入到伺服器本地
                    destination = open(os.path.join("./media/upload", file.name), 'wb+')
                    for chunk in file.chunks():
                        destination.write(chunk)
                    destination.close()

            return HttpResponseRedirect('/UploadFile/upload-file')
    # 列表頁
    else:
        files = File.objects.all()  #查詢所有資料
        form = FileForm()
        context = {
            'files': files,
            'form': form
        }            
        return render(request, 'uploadfile/upload-file.html', context)

# 下載檔案
def download_file(request, name):
    file_result = File.objects.filter(name=name)
    # 如果檔案存在，就下載檔案
    if file_result:
        file = list(file_result)[0]
        # 檔名稱及路徑
        name = file.name
        path = file.path
        # 讀取檔案
        file = open(path, 'rb')
        response = FileResponse(file)
        # 使用urlquote對檔名稱進行編碼
        response['Content-Disposition'] = 'attachment;filename="%s"' % urlquote(name)
        return response
    else:
        return HttpResponse('[%s] 檔案不存在!' %name)