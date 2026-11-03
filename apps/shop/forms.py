from django import forms 

from shop.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'text', 'price']
        widgets = {
        'product_name': forms.TextInput(attrs={
        'placeholder': "Максимальная длина 200 символов"
    }),
    'text': forms.Textarea(attrs={
        'rows': 3,
        'cols': 20
    }),
    'price': forms.NumberInput()
    }
    labels = {
        'product_name': 'Название товара:',
        'text': 'Описание:',
        'price': 'цена:'
    }

    def clean_product_name(self):
        product_name = self.cleaned_data['product_name'].strip()

        if len(product_name) < 6:
            raise forms.ValidationError("Название не должно быть короче 6 символов")

        return product_name


    def clean_price(self):
        price = self.cleaned_data['price']

        if price <= 0:
            raise forms.ValidationError("укажите корректную цену товара")

        return price