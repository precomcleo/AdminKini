from django.shortcuts import render
from Commodity.models import Item 

# Create your views here.
def CommodityPage(request):
    Commodity = Item.objects.all()[:30]
    context = {'Commodity':Commodity}
    return render(request, 'commodity/commodity_list.html', context)