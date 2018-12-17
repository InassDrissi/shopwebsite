from django.shortcuts import render ,get_object_or_404
from .models import Shop,Product

def index(request):
    all_shops = Shop.objects.all()
    return render(request, 'mall/index.html', {'all_shops': all_shops})


def detail(request, shop_id):

    shop = get_object_or_404(Shop, pk=shop_id)
    return render(request, 'mall/detail.html', {'shop': shop})

