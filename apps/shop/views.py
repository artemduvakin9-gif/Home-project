from django.shortcuts import get_object_or_404, redirect, render

from shop.forms import ProductForm
from shop.models import Product

def home_page_view(request):
    products = Product.objects.all()
    return render(request, 'shop/pages/index.html', context={'products': products})

def get_product_detail_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'shop/pages/product_detail.html', context={"product": product})





def product_add_view(request):
    form = ProductForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            product = form.save()
            return redirect('shop:product_detail', product_id=product.id)

    return render(request, 'shop/pages/product_add.html', {"form": form})


