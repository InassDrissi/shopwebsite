from django.shortcuts import render ,get_object_or_404
from .models import Shop,Product


def index(request):

    all_shops = Shop.objects.all()
    return render(request, 'mall/index.html', {'all_shops': all_shops})


def detail(request, shop_id):

    shop = get_object_or_404(Shop, pk=shop_id)
    return render(request, 'mall/detail.html', {'shop': shop})


def favorite(request, shop_id):

    all_shops = Shop.objects.all()
    shop = get_object_or_404(Shop, pk=shop_id)
    shop.is_favorite = True
    shop.save()
    return render(request, 'mall/index.html', {'all_shops': all_shops})


def nofavorite(request, shop_id):

    all_shops = Shop.objects.all()
    shop = get_object_or_404(Shop, pk=shop_id)
    shop.is_favorite = False
    shop.save()
    return render(request, 'mall/index.html', {'all_shops': all_shops})


def preferred(request):

    all_shops = Shop.objects.all()
    return render(request, 'mall/preferred.html',{'all_shops': all_shops})


