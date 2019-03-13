from django.shortcuts import render
from Order.models import Inventory 
from django.contrib.auth.decorators import login_required
from Order.models import Customer, OrderStatus
from django.http import HttpResponseRedirect
from .forms import CustomerForm, InventoryForm

# Create your views here.
@login_required
def OrderPage(request):
    Order = Inventory.objects.all()[:30]
    
    inventory_form = InventoryForm(request.POST or None)
    if inventory_form.is_valid(): #用來驗證資料是否正確
        inventory_form.save()
        inventory_form = InventoryForm() #清空form

    customer_form = CustomerForm(request.POST or None)

    context = {
        'Order':Order,
        'inventory_form' : inventory_form,
        'customer_form' : customer_form
    }
    return render(request, 'order/order_list.html', context)



def shipped(request):
    if request.method == 'POST': 
        out = request.POST.getlist('shipped')
        for i in out:
            shipment_status = Customer.objects.get(pk=i)
            if shipment_status.Status == OrderStatus.objects.get(Status="訂單生成") :
                shipped_ready = OrderStatus.objects.get(Status="已出貨")
                shipment_status.Status = shipped_ready
                shipment_status.save()

            elif shipment_status.Status == OrderStatus.objects.get(Status="已出貨"):
                shipped_ready = OrderStatus.objects.get(Status="訂單生成")
                shipment_status.Status = shipped_ready
                shipment_status.save()

        return HttpResponseRedirect('/Order/')
        #return render(request, "order/tt.html", {'out':re})

def addbuyer(request):
    Inventory_id = request.POST.getlist('addbuyer')
    customer_form = CustomerForm(request.POST, initial={'Inventory_id': Inventory_id})
    if customer_form.is_valid():
        customer_form.save()
    return HttpResponseRedirect('/Order/')


def order_create_view(request):    #--a. 成功新增後清空表單--
    pass
    # form = CustomerForm(request.POST or None)
    # if form.is_valid(): #用來驗證資料是否正確
    #     form.save()
    #     form = CustomerForm() #清空form
    #     #return redirect(store.get_absolute_url())
    # context = {
    #      'form' : form
    # }
    # return HttpResponseRedirect('/Order/')