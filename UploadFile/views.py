from django.shortcuts import render, redirect
from .forms import UploadModelForm
from UploadFile.models import Photo
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    photos = Photo.objects.all()  #查詢所有資料
    form = UploadModelForm()
    if request.method == "POST":
        form = UploadModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/UploadFile')
    context = {
        'photos': photos,
        'form': form
    }
    return render(request, 'uploadfile/uploadfile.html', context)

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