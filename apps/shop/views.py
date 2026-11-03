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
    if request.method == "POST":
        form = ProductForm(request.POST)

        if form.is_valid():
            product = Product.objects.create(
                product_name=form.cleaned_data['product_name'],
                text=form.cleaned_data['text'],
                price=form.cleaned_data['price']
            )

            return redirect('shop:product_detail', product_id=product.id)

        return render(request, 'shop/pages/product_add.html', {"form": form})

    form = ProductForm()
    return render(request, 'shop/pages/product_add.html', {"form": form})



    #     errors = {}
    #     # if not product_name:
    #     #     errors['product_name'] = 'Название товара обязателен к заполнению'
    #     if len(product_name) < 6:
    #         errors['product_name'] = 'Название товара должно состоять из больше 6 символов'
    #     if not text:
    #         errors['text'] = 'Описание обязательно к заполнению'
    #     if price <= '0':
    #         errors['price'] = 'введите корректную цену для товара'

    #     if errors:
    #         context = {
    #             'errors': errors,
    #             'product_name': product_name,
    #             'text': text,
    #             'price': price
    #         }
    #         return render(request, 'shop/pages/product_add.html', context)

    #     product = Product.objects.create(product_name=product_name, text=text, price=price)
    #     return redirect('shop:product_detail', product_id=product.id)

    # return render(request, 'shop/pages/product_add.html')


