from django.shortcuts import redirect, render
from .models import Vendor
from django.contrib.auth.decorators import login_required

# Create your views here.

from django.views.generic import ListView, DetailView # 新增
class VendorListView(ListView):         #繼承ListView
    model = Vendor
    template_name = 'ven/vendor_list.html'

class VendorDetailView(DetailView):     #繼承DetailView
    model = Vendor
    template_name = 'ven/vendor_detail.html'

@login_required
def vendor_list(request):
    vendors = Vendor.objects.all()
    context = {'vendor_list': vendors} # 建立 Dict對應到Vendor的資料，
    #return render(request, 'vendor/vendor_list.html', {'vendors': vendors}) #額外的 context data，可以在處理 template 時使用
    return render(request, 'vendor/vendor_list.html', context)

from django.http import Http404
@login_required
def vendor_detail(request, pk):
    try:
        vendor = Vendor.objects.get(pk=pk)
    except Vendor.DoesNotExist:
        raise Http404
    return render(request, 'vendor/vendor_detail.html', {'vendor': vendor})

# from django.shortcuts import get_object_or_404 # 新增
# def vendor_detail(request, id):
#     vendor_list = get_object_or_404(Vendor, id=id)
#     # try:
#     #     vendor_list = Vendor.objects.get(id=id)
#     # except Vendor.DoesNotExist:
#     #     raise Http404
#     context = {
#         'vendor_list': vendor_list
#     }
#     return render(request, 'vendor/vendor_detail.html', context)

from .forms import VendorForm # 要記得 import 相對應的 Model Form 唷!
from django.views.generic import CreateView
class VendorCreateView(CreateView):
    form_class = VendorForm
    #model = Vendor
    #fields='__all__'
    template_name = 'ven/vendor_create.html'

@login_required
def vendor_create_view(request):    #--a. 成功新增後清空表單--
    form = VendorForm(request.POST or None)
    if form.is_valid(): #用來驗證資料是否正確
        form.save()
        #form = VendorForm() #清空form
        #return redirect(store.get_absolute_url())
    context = {
        'form' : form
    }
    return render(request, "vendor/vendor_create.html", context)

def is_authenticated(user):
    if callable(user.is_authenticated):
        return user.is_authenticated()
    return user.is_authenticated


from django.forms.models import modelform_factory
@login_required
def re_vendor_create_view(request): #--b. 成功新增後導向產品清單頁，失敗就停留在新增頁--
    VendorForm = modelform_factory(Vendor, fields=('__all__'))
    if request.method == 'POST':
        form = VendorForm(request.POST)
        # if form.is_valid():
        #     vendor = form.save()
        #     return redirect(vendor.get_absolute_url())
        
        if form.is_valid():
            vendor = form.save(commit=False)
            if request.user.is_authenticated:
                vendor.owner = request.user
            vendor.save()
            return redirect(vendor.get_absolute_url())

    else:
        form = VendorForm()
    return render(request, 'vendor/vendor_create.html', {'form': form})


from django.views.generic import UpdateView # 新增
class VendorUpdateView(UpdateView):
    form_class = VendorForm
    template_name = 'ven/vendor_create.html'
    queryset = Vendor.objects.all() # 這很重要

@login_required
def vendor_update(request, pk): #--廠商資料更新--
    try:
        vendor = Vendor.objects.get(pk=pk)
    except Vendor.DoesNotExist:
        raise Http404
    VendorForm = modelform_factory(Vendor, fields=('__all__'))
    if request.method == 'POST':
        form = VendorForm(request.POST, instance=vendor)
        if form.is_valid():
            vendor = form.save()
            return redirect(vendor.get_absolute_url())
    else:
        form = VendorForm(instance=vendor)
    return render(request, 'vendor/vendor_update.html', {
        'form': form, 'vendor': vendor,
    })


from django.http import HttpResponseForbidden
from django.views.decorators.http import require_http_methods #這個 view 可以接收的 HTTP methods
from django.contrib.auth.decorators import login_required #只有已登入使用者才能進入這個 view
from django.http import HttpResponse

@login_required
@require_http_methods(['POST', 'DELETE'])
def vendor_delete(request, pk):
    try:
        vendor = Vendor.objects.get(pk=pk)
    except Vendor.DoesNotExist:
        raise Http404
    if vendor.can_user_delete(request.user):
        vendor.delete()
        if request.is_ajax():
            return HttpResponse()
        return redirect('/Vendor')
    return HttpResponseForbidden()