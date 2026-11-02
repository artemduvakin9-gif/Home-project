from django.shortcuts import get_object_or_404, redirect, render

from shop.models import Product

def home_page_view(request):
    products = Product.objects.all()
    return render(request, 'shop/index.html', context={'products': products})

def get_product_detail_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'shop/product_detail.html', context={"product": product})

def product_add_view(request):
    if request.method == "GET":
        return render(request, 'shop/product_add.html')

    elif request.method == "POST":
        product = Product.objects.create(
            product_name = request.POST['title'],
            text = request.POST['text'],
            price = request.POST['price']
            )

        return redirect('shop:product_detail', product_id=product.id)


