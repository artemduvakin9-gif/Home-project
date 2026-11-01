from django.shortcuts import get_object_or_404 ,render

from shop.models import Product

def home_page_view(request):
    products = Product.objects.all()
    return render(request, 'shop/index.html', context={'products': products})

def get_product_detail_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'shop/product_detail.html', context={"product": product})

