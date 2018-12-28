from django.shortcuts import render
from Commodity.models import Item 
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def CommodityPage(request):
    Commodity = Item.objects.all()[:30]
    context = {'Commodity':Commodity}
    return render(request, 'commodity/commodity_list.html', context)