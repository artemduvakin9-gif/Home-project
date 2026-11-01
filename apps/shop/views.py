from django.shortcuts import render

from shop.models import Product

def home_page_view(request):
    products = Product.objects.all()
    return render(request, 'shop/index.html', context={'products': products})
