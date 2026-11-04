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

    return render(
        request,
        'shop/pages/product_form.html', 
        {
        "form": form,
        "product_name": "Добавить товар",
        "h1": "Новый товар",
        "submit_button_text": "Добавить",
        }
    )

def product_edit_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    extra_context={
        "product_name": "Редактировать товар",
        "h1": "Редактирование",
        "submit_button_text": "Сохранить",
    }

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)

        if form.is_valid():
            form.save()
            return redirect("shop:product_detail", product_id=product.id)

        return render(
            request,
            'shop/pages/product_form.html',
            context={
                "form": form,
                **extra_context,
                }
            )

    form = ProductForm(instance=product)
    return render(
        request,
        'shop/pages/product_form.html',
        context={
        "form": form,
        **extra_context
            }
        )


